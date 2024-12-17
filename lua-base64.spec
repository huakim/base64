%define luarocks_pkg_name base64
%define luarocks_pkg_version scm-0
%define luarocks_pkg_prefix base64-scm-0
%define luarocks_pkg_major scm
%define luarocks_pkg_minor 0

Name: lua-base64
Version: %{luarocks_pkg_major}
Release: %{luarocks_pkg_minor}
Summary: Pure Lua base64 encoder/decoder
Url: https://github.com/huakim/lua-base64
License: MIT/Public Domain
Source0: base64-scm-0.tar.gz
Source1: base64-scm-0.rockspec
BuildRequires: lua-rpm-macros
Requires(postun): alternatives
Requires(post): alternatives
Provides: %{luadist %{luarocks_pkg_name} = %{luarocks_pkg_version}}
%global __luarocks_requires %{_bindir}/true
%global __luarocks_provides %{_bindir}/true
%{?luarocks_subpackages:%luarocks_subpackages -f}

%description
Pure Lua base64 encoder/decoder. Works with Lua 5.1+ and LuaJIT. Fallbacks to pure Lua bit operations if bit/bit32/native bit operators are not available.

%prep
%autosetup -p1 -n %{luarocks_pkg_prefix}
%luarocks_prep

%generate_buildrequires
%{?luarocks_buildrequires_echo}
%if %{with check}
%luarocks_generate_buildrequires -c -b
%else
%luarocks_generate_buildrequires -b 
%endif

%build
%{?custom_build}
%if %{defined luarocks_subpackages_build}
%{luarocks_subpackages_build}
%else
%if %{defined luarocks_pkg_build}
%luarocks_pkg_build %{lua_version}
%else
%luarocks_build --local
%endif
%endif

%install
%{?custom_install}
%if %{defined luarocks_subpackages_install}
%{luarocks_subpackages_install}
%else
%if %{defined luarocks_pkg_install}
%luarocks_pkg_install %{lua_version}
%else
%luarocks_install %{luarocks_pkg_prefix}.*.rock
%endif
%endif
%{?lua_generate_file_list}

%check
%if %{with check}
%{?luarocks_check}
%endif

%files %{?lua_files}%{!?lua_files:-f lua_files.list}
