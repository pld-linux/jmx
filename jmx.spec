Summary:	Java Management Extensions
Summary(pl):	Rozszerzenia zarz±dzania do Javy
Name:		jmx
Version:	1.0.1
Release:	1
License:	See http://java.sun.com/products/JavaManagement/ for details!
Group:		Development/Languages/Java
Source0:	jmx-1_0-ri_bin.zip
URL:		http://java.sun.com/products/JavaManagement/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Java Management Extensions.

%description -l pl
Java Management Extensions - rozszerzenia zarz±dzania do Javy.

%package doc
Summary:	Documentation for Java Management Extensions
Summary(pl):	Dokumentacja do Java Management Extensions
Group:		Development/Languages/Java

%description doc
Documentation for Java Management Extensions.

%description doc -l pl
Dokumentacja do Java Management Extensions.

%prep
%setup -q -n jmx-1_0_1-ri_bin

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install jmx/lib/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc jmx/doc jmx/examples jmx/index.html
