Summary:	Java Management Extensions
Summary(pl):	Rozszerzenia zarz±dzania do Javy
Name:		jmx
Version:	1.2.1
Release:	1
License:	restricted, non-distributable (Sun Binary Code License - see URL)
Group:		Development/Languages/Java
# download through forms from http://java.sun.com/products/JavaManagement/download.html
Source0:	%{name}-%(echo %{version}| tr . _)-ri.zip
URL:		http://java.sun.com/products/JavaManagement/
NoSource:	0
Requires:	jre
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
%setup -q -n %{name}-%(echo %{version}| tr . _)-bin

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install lib/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc doc examples
