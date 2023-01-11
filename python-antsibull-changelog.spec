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

Name: python-antsibull-changelog
Epoch: 100
Version: 0.19.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Ansible Changelog Tool
License: GPL-3.0-only
URL: https://github.com/ansible-community/antsibull-changelog/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
A changelog generator used by ansible-core and Ansible collections.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-antsibull-changelog
Summary: Ansible Changelog Tool
Requires: python3
Requires: python3-docutils
Requires: python3-packaging
Requires: python3-PyYAML
Requires: python3-rstcheck >= 3
Requires: python3-semantic_version
Provides: python3-antsibull-changelog = %{epoch}:%{version}-%{release}
Provides: python3dist(antsibull-changelog) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-antsibull-changelog = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(antsibull-changelog) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-antsibull-changelog = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(antsibull-changelog) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-antsibull-changelog
A changelog generator used by ansible-core and Ansible collections.

%files -n python%{python3_version_nodots}-antsibull-changelog
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-antsibull-changelog
Summary: Ansible Changelog Tool
Requires: python3
Requires: python3-docutils
Requires: python3-packaging
Requires: python3-PyYAML
Requires: python3-rstcheck >= 3
Requires: python3-semantic_version
Provides: python3-antsibull-changelog = %{epoch}:%{version}-%{release}
Provides: python3dist(antsibull-changelog) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-antsibull-changelog = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(antsibull-changelog) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-antsibull-changelog = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(antsibull-changelog) = %{epoch}:%{version}-%{release}

%description -n python3-antsibull-changelog
A changelog generator used by ansible-core and Ansible collections.

%files -n python3-antsibull-changelog
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-antsibull-changelog
Summary: Ansible Changelog Tool
Requires: python3
Requires: python3-docutils
Requires: python3-packaging
Requires: python3-pyyaml
Requires: python3-rstcheck >= 3
Requires: python3-semantic_version
Provides: python3-antsibull-changelog = %{epoch}:%{version}-%{release}
Provides: python3dist(antsibull-changelog) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-antsibull-changelog = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(antsibull-changelog) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-antsibull-changelog = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(antsibull-changelog) = %{epoch}:%{version}-%{release}

%description -n python3-antsibull-changelog
A changelog generator used by ansible-core and Ansible collections.

%files -n python3-antsibull-changelog
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
