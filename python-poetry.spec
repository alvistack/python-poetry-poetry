# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-poetry
Epoch: 100
Version: 1.3.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Python dependency management and packaging made easy
License: MIT
URL: https://github.com/python-poetry/poetry/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Poetry helps you declare, manage and install dependencies of Python
projects, ensuring you have the right stack everywhere.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/poetry/__init__.py
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-poetry
Summary: Python dependency management and packaging made easy
Requires: python3
Requires: python3-backports-cached-property >= 1.0.2
Requires: python3-cachecontrol >= 0.12.9
Requires: python3-cleo >= 2.0.0
Requires: python3-crashtest >= 0.4.1
Requires: python3-dulwich >= 0.20.46
Requires: python3-filelock >= 3.8.0
Requires: python3-html5lib >= 1.0
Requires: python3-importlib-metadata >= 4.4
Requires: python3-jsonschema >= 4.10.0
Requires: python3-keyring >= 23.9.0
Requires: python3-packaging >= 20.4
Requires: python3-pexpect >= 4.7.0
Requires: python3-pkginfo >= 1.5
Requires: python3-platformdirs >= 2.5.2
Requires: python3-poetry-core >= 1.4.0
Requires: python3-poetry-plugin-export >= 1.2.0
Requires: python3-requests >= 2.18
Requires: python3-requests-toolbelt >= 0.9.1
Requires: python3-shellingham >= 1.5
Requires: python3-tomli >= 2.0.1
Requires: python3-tomlkit >= 0.11.1
Requires: python3-trove-classifiers >= 2022.5.19
Requires: python3-urllib3 >= 1.26.0
Requires: python3-virtualenv >= 20.4.3
Provides: poetry = %{epoch}:%{version}-%{release}
Provides: python3-poetry = %{epoch}:%{version}-%{release}
Provides: python3dist(poetry) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-poetry = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(poetry) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-poetry = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(poetry) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-poetry
Poetry helps you declare, manage and install dependencies of Python
projects, ensuring you have the right stack everywhere.

%files -n python%{python3_version_nodots}-poetry
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-poetry
Summary: Python dependency management and packaging made easy
Requires: python3
Requires: python3-backports-cached-property >= 1.0.2
Requires: python3-cachecontrol >= 0.12.9
Requires: python3-cleo >= 2.0.0
Requires: python3-crashtest >= 0.4.1
Requires: python3-dulwich >= 0.20.46
Requires: python3-filelock >= 3.8.0
Requires: python3-html5lib >= 1.0
Requires: python3-importlib-metadata >= 4.4
Requires: python3-jsonschema >= 4.10.0
Requires: python3-keyring >= 23.9.0
Requires: python3-packaging >= 20.4
Requires: python3-pexpect >= 4.7.0
Requires: python3-pkginfo >= 1.5
Requires: python3-platformdirs >= 2.5.2
Requires: python3-poetry-core >= 1.4.0
Requires: python3-poetry-plugin-export >= 1.2.0
Requires: python3-requests >= 2.18
Requires: python3-requests-toolbelt >= 0.9.1
Requires: python3-shellingham >= 1.5
Requires: python3-tomli >= 2.0.1
Requires: python3-tomlkit >= 0.11.1
Requires: python3-trove-classifiers >= 2022.5.19
Requires: python3-urllib3 >= 1.26.0
Requires: python3-virtualenv >= 20.4.3
Provides: poetry = %{epoch}:%{version}-%{release}
Provides: python3-poetry = %{epoch}:%{version}-%{release}
Provides: python3dist(poetry) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-poetry = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(poetry) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-poetry = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(poetry) = %{epoch}:%{version}-%{release}

%description -n python3-poetry
Poetry helps you declare, manage and install dependencies of Python
projects, ensuring you have the right stack everywhere.

%files -n python3-poetry
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
