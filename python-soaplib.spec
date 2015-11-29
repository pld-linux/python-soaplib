# TODO
# - better group

%define		_rc	beta2
%define 	module	soaplib
Summary:	A transport and architecture agnostic soap (de)serialization library that focuses on making small, rpc-like messaging work
Name:		python-%{module}
Version:	2.0.0
Release:	0.1_%{_rc}
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}-%{_rc}.tar.gz
# Source0-md5:	294bc8db05011bfa14e00a6a9368e2ae
URL:		http://pypi.python.org/pypi/soaplib
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires(post,preun):	/sbin/chkconfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple, easily extendible soap library that provides several
useful tools for creating and publishing soap web services in python.
This package features on-demand wsdl generation for the published
services, a wsgi-compliant web application, support for complex class
structures, binary attachments, and a simple framework for creating
additional serialization mechanisms.

This project uses lxml as it's XML API, providing full namespace
support.

%prep
%setup -q -n %{module}-%{version}-%{_rc}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO

%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
%{py_sitescriptdir}/%{module}-*pth
