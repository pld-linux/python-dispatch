#
# TODO:
# - pl
# - fix instalation (setup.py needs rewriting)
#
%define 	module	dispatch
%define		srcname	PyDispatcher
%define		alpha	a1
#
Summary:	Python module providing a multiple-producer-multiple-consumer signal-registration and routing infrastructure
Name:		python-%{module}
Version:	1.0.2
Release:	4
License:	BSD-like
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pydispatcher/%{srcname}-%{version}.tar.gz
# Source0-md5:	f48c3662759b94ce9c020925316b2036
URL:		http://pydispatcher.sf.net/
BuildRequires:	python
Requires:	python-modules >= 2.2.3
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyDispatcher provides the Python programmer with a
multiple-producer-multiple-consumer signal-registration and routing
infrastructure for use in multiple contexts. The mechanism of
PyDispatcher started life as a highly rated recipe in the Python
Cookbook. The SourceForge project aims to include various enhancements
to the recipe developed during use in various applications.

%package examples
Summary:	Examples and tests for PyDispatcher
Group:          Development/Languages/Python
Requires:       %{name} = %{version}-%{release}

%description examples
PyDispatcher provides the Python programmer with a
multiple-producer-multiple-consumer signal-registration and routing
infrastructure for use in multiple contexts. The mechanism of
PyDispatcher started life as a highly rated recipe in the Python
Cookbook. The SourceForge project aims to include various enhancements
to the recipe developed during use in various applications.

This module contains an example and test programs.

%prep
%setup -q -n %{srcname}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%{__install} -d $RPM_BUILD_ROOT/%{_examplesdir}/%{name}
mv  $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/{examples,tests} \
    $RPM_BUILD_ROOT/%{_examplesdir}/%{name}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}
rm -fr $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/{*.py,MANIFEST.in,PKG-INFO,docs,license.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* license.txt
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
