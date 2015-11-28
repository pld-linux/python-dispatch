#
# TODO:
# - pl
# - fix instalation (setup.py needs rewriting)
#
%define 	module	dispatch
%define		srcname	PyDispatcher
%define		alpha	a1
#
Summary:	Python module providing signal-registration and routing infrastructure
Summary(pl.UTF-8):	Moduł Pythona dostarczający infrastrukturę rejestrowania i przekazywania sygnałów
Name:		python-%{module}
Version:	1.0.2
Release:	6
License:	BSD-like
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pydispatcher/%{srcname}-%{version}.tar.gz
# Source0-md5:	f48c3662759b94ce9c020925316b2036
URL:		http://pydispatcher.sourceforge.net/
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
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

%description -l pl.UTF-8
PyDispatcher dostarcza programistom Pythona infrastrukturę
rejestrowania i przekazywania sygnałów w środowisku z wieloma
producentami i wieloma konsumentami do używania w wielu kontekstach.
Mechanizm PyDispatchera rozpoczął swoje życie jako wysoko wyceniony
opis w Python Cookbook. Celem projektu SourceForge jest dołączenie do
opisu różnych rozszerzeń tworzonych podczas używania w różnych
aplikacjach.

%package examples
Summary:	Examples and tests for PyDispatcher
Summary(pl.UTF-8):	Przykłady i testy dla PyDispatchera
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description examples
PyDispatcher provides the Python programmer with a
multiple-producer-multiple-consumer signal-registration and routing
infrastructure for use in multiple contexts. The mechanism of
PyDispatcher started life as a highly rated recipe in the Python
Cookbook. The SourceForge project aims to include various enhancements
to the recipe developed during use in various applications.

This package contains example and test programs.

%description examples -l pl.UTF-8
PyDispatcher dostarcza programistom Pythona infrastrukturę
rejestrowania i przekazywania sygnałów w środowisku z wieloma
producentami i wieloma konsumentami do używania w wielu kontekstach.
Mechanizm PyDispatchera rozpoczął swoje życie jako wysoko wyceniony
opis w Python Cookbook. Celem projektu SourceForge jest dołączenie do
opisu różnych rozszerzeń tworzonych podczas używania w różnych
aplikacjach.

Ten pakiet zawiera programy przykładowe i testowe.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv  $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/{examples,tests} \
    $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
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
%{_examplesdir}/%{name}-%{version}
