local comm = require "comm"
local string = require "string"
local table = require "table"
local shortport = require "shortport"
local nmap = require "nmap"
local stdnse = require "stdnse"
local U = require "lpeg-utility"

description = [[
Utiliza el header Server del servidor HTTP para obtener informacion sobre la version del servidor utilizado.
]]

---
--@output
-- PORT   STATE SERVICE VERSION
-- 80/tcp open  http    Servidor no Identificado 1.0
--
-- PORT   STATE SERVICE VERSION
-- 80/tcp open  http    Servidor no Identificado 1.0
-- |_ Servidor http:  	Servidor no Identificado 1.0
--
--@xmloutput
--<table key="Server">
--  <elem>Servidor no Identificado 1.0</elem>
--  <elem>SomeOther Server</elem>
--</table>

author = "Dialid Ceron"
license = "Plan de Becarios de Seguridad Informatica CERT UNAM"
categories = {"version"}
dependencies = {"https-redirect"}

portrule = function(host, port)
  return (shortport.http(host,port) and nmap.version_intensity() >= 7)
end

action = function(host, port)
  local responses = {}
  if port.version and port.version.service_fp then
    -- Itera para recibir respuestas HTTP
    for _, p in ipairs({"GetRequest", "GenericLines", "HTTPOptions",
      "FourOhFourRequest", "NULL", "RTSPRequest", "Help", "SIPOptions"}) do
      responses[#responses+1] = U.get_response(port.version.service_fp, p)
    end
  end
  if #responses == 0 then
    local socket, result = comm.tryssl(host, port, "GET / HTTP/1.0\r\n\r\n")

    if (not socket) then
      return nil
    end
    socket:close()
    responses[1] = result
  end
  --IIS manda diferente los headers del servidor
  local socket, result = comm.tryssl(host, port,
    ("GET / HTTP/1.1\r\nHost: %s\r\n\r\n"):format(stdnse.get_hostname(host)))
  if socket then
    socket:close()
    responses[#responses+1] = result
  end

  port.version = port.version or {}

  local headers = {}
  for _, result in ipairs(responses) do
    if string.match(result, "^HTTP/1.[01] %d%d%d") then

      local http_server = string.match(result, "\n[Ss][Ee][Rr][Vv][Ee][Rr]:[ \t]*(.-)\r?\n")

      --Evitamos modificar la informacion de version si el escaneo -sV ya encontro un match
      if port.version.product == nil and (port.version.name_confidence or 0) <= 3 then
        port.version.service = "http"
        port.version.product = http_server
	--Cambiar "softmatched" permite al fingerprint del servidor ser impreso
        nmap.set_port_version(host, port, "softmatched")
      elseif port.version.product == http_server then
        -- Si ya detectamos exactamente esto, no  hay necesidad de reportarlo
        http_server = nil
      end

      if http_server then
        headers[http_server] = true
      end
    end
  end

  local out = {}
  local out_s = {}
  for s, _ in pairs(headers) do
    out[#out+1] = s
    out_s[#out_s+1] = s == "" and "<empty>" or s
  end
  if next(out) then
    table.sort(out)
    table.sort(out_s)
    return out, ((#out > 1) and "\n  " or "") .. table.concat(out_s, "\n  ")
  end
end
