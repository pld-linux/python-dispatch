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
Version:	1.0.0
Release:	0.%{alpha}
License:	BSD-like
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pydispatcher/%{srcname}-%{version}%{alpha}.zip
# Source0-md5:	716b67e192dc0ff7561a84744898aa17
URL:		http://pydispatcher.sf.net/
Requires:	python-modules >= 2.2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyDispatcher provides the Python programmer with a
multiple-producer-multiple-consumer signal-registration and routing
infrastructure for use in multiple contexts. The mechanism of
PyDispatcher started life as a highly rated recipe in the Python
Cookbook. The SourceForge project aims to include various enhancements
to the recipe developed during use in various applications.

%prep
%setup -q -n %{srcname}-%{version}%{alpha}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

#rm $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/*.py
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* license.txt
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*
