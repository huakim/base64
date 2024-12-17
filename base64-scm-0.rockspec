package = "base64"
version = "scm-0"
source = {
   url = "git://github.com/huakim/lua-base64"
}
description = {
   summary = "Pure Lua base64 encoder/decoder",
   detailed = [[
Pure Lua base64 encoder/decoder. Works with Lua 5.1+ and LuaJIT. Fallbacks to pure Lua bit operations if bit/bit32/native bit operators are not available.]],
   homepage = "https://github.com/huakim/lua-base64",
   license = "MIT/Public Domain"
}
dependencies = {}
build = {
   type = "builtin",
   modules = {
      base64 = "base64.lua",
   }
}
