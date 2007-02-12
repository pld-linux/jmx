Summary:	Java Management Extensions
Summary(pl.UTF-8):   Rozszerzenia zarządzania do Javy
Name:		jmx
Version:	1.2.1
Release:	1
License:	restricted, non-distributable (Sun Community Source License - see URL)
Group:		Development/Languages/Java
# download through forms from http://java.sun.com/products/JavaManagement/download.html
Source0:	%{name}-%(echo %{version}| tr . _)-scsl.zip
Patch0:		%{name}-build.patch
URL:		http://java.sun.com/products/JavaManagement/
NoSource:	0
BuildRequires:	ant
BuildRequires:	jdk >= 1.4
Requires:	jre >= 1.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java Management Extensions.

%description -l pl.UTF-8
Java Management Extensions - rozszerzenia zarządzania do Javy.

%package doc
Summary:	Documentation for Java Management Extensions
Summary(pl.UTF-8):   Dokumentacja do Java Management Extensions
Group:		Development/Languages/Java

%description doc
Documentation for Java Management Extensions.

%description doc -l pl.UTF-8
Dokumentacja do Java Management Extensions.

%prep
%setup -q -n %{name}-%(echo %{version}| tr . _)-src
%patch0 -p1

%build
ant

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}
install build/lib/jmxri.jar $RPM_BUILD_ROOT%{_javadir}
install lib/jmxtools.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc doc examples
