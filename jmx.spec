Summary:	Java Management Extensions
Name:		jmx
Version:	1.0.1
Release:	1
License:	See http://java.sun.com/products/JavaManagement for details!!!
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	jmx-1_0-ri_bin.zip
URL:		http://java.sun.com/products/JavaManagement
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Java Management Extensions

%package doc
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Summary:	Documentation for Java Management Extensions

%description doc
Documentation for Java Management Extensions

%prep
%setup -q -n jmx-1_0_1-ri_bin

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_javalibdir}
cp jmx/lib/*.jar $RPM_BUILD_ROOT/%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_javalibdir}
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc jmx/doc jmx/examples jmx/index.html
