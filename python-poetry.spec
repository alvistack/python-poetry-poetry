%global debug_package %{nil}

Name: python-poetry
Epoch: 100
Version: 1.1.12
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
Requires: python3-cachy >= 0.3.0
Requires: python3-cleo >= 0.8.1
Requires: python3-clikit >= 0.6.2
Requires: python3-html5lib >= 1.0
Requires: python3-importlib-metadata >= 1.6.0
Requires: python3-packaging >= 20.4
Requires: python3-pexpect >= 4.7.0
Requires: python3-pkginfo >= 1.4
Requires: python3-poetry-core >= 1.0.7
Requires: python3-requests >= 2.18
Requires: python3-requests-toolbelt >= 0.9.1
Requires: python3-shellingham >= 1.1
Requires: python3-tomlkit >= 0.7.0
Requires: python3-virtualenv >= 20.0.26
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
Requires: python3-cachy >= 0.3.0
Requires: python3-cleo >= 0.8.1
Requires: python3-clikit >= 0.6.2
Requires: python3-html5lib >= 1.0
Requires: python3-importlib-metadata >= 1.6.0
Requires: python3-packaging >= 20.4
Requires: python3-pexpect >= 4.7.0
Requires: python3-pkginfo >= 1.4
Requires: python3-poetry-core >= 1.0.7
Requires: python3-requests >= 2.18
Requires: python3-requests-toolbelt >= 0.9.1
Requires: python3-shellingham >= 1.1
Requires: python3-tomlkit >= 0.7.0
Requires: python3-virtualenv >= 20.0.26
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
