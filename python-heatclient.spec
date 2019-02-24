#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : python-heatclient
Version  : 1.17.0
Release  : 41
URL      : http://tarballs.openstack.org/python-heatclient/python-heatclient-1.17.0.tar.gz
Source0  : http://tarballs.openstack.org/python-heatclient/python-heatclient-1.17.0.tar.gz
Source99 : http://tarballs.openstack.org/python-heatclient/python-heatclient-1.17.0.tar.gz.asc
Summary  : Python client library for Heat
Group    : Development/Tools
License  : Apache-2.0
Requires: python-heatclient-bin = %{version}-%{release}
Requires: python-heatclient-license = %{version}-%{release}
Requires: python-heatclient-python = %{version}-%{release}
Requires: python-heatclient-python3 = %{version}-%{release}
Requires: Babel
Requires: PyYAML
Requires: cliff
Requires: iso8601
Requires: keystoneauth1
Requires: osc-lib
Requires: oslo.i18n
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: python-swiftclient
Requires: requests
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/python-heatclient.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package bin
Summary: bin components for the python-heatclient package.
Group: Binaries
Requires: python-heatclient-license = %{version}-%{release}

%description bin
bin components for the python-heatclient package.


%package license
Summary: license components for the python-heatclient package.
Group: Default

%description license
license components for the python-heatclient package.


%package python
Summary: python components for the python-heatclient package.
Group: Default
Requires: python-heatclient-python3 = %{version}-%{release}

%description python
python components for the python-heatclient package.


%package python3
Summary: python3 components for the python-heatclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-heatclient package.


%prep
%setup -q -n python-heatclient-1.17.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551035574
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-heatclient
cp LICENSE %{buildroot}/usr/share/package-licenses/python-heatclient/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/heat

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-heatclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
