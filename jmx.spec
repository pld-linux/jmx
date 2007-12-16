#
# Conditional build:
%bcond_with	scsl	# use SCSL-licensed sources (which need registration)
#
%include	/usr/lib/rpm/macros.java
%define		fver	%(echo %{version} | tr . _)
Summary:	Java Management Extensions
Summary(pl.UTF-8):	Rozszerzenia zarządzania do Javy
Name:		jmx
Version:	1.2.1
Release:	1
License:	restricted, non-distributable (Sun Community Source License - see URL)
Group:		Development/Languages/Java
# download through forms from http://java.sun.com/products/JavaManagement/download.html
Source0:	%{name}-%{fver}-ri.zip
# NoSource0-md5:	2775b37b00b4da79115b222737b6df9c
NoSource:	0
%if %{with scsl}
Source1:	%{name}-%{fver}-scsl.zip
# NoSource1-md5:	de1a800156998f4ef98bcdef4421f312
NoSource:	1
%endif
Patch0:		%{name}-build.patch
URL:		http://java.sun.com/products/JavaManagement/
%{?with_scsl:BuildRequires:	ant}
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre >= 1.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java Management Extensions.

%description -l pl.UTF-8
Java Management Extensions - rozszerzenia zarządzania do Javy.

%package javadoc
Summary:	Documentation for Java Management Extensions
Summary(pl.UTF-8):	Dokumentacja do Java Management Extensions
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jmx-doc

%description javadoc
Documentation for Java Management Extensions.

%description javadoc -l pl.UTF-8
Dokumentacja do Java Management Extensions.

%package tools
Summary:	JMX additional classes (com.sun.jdmk in jmxtools.jar)
Summary(pl.UTF-8):	Dodatkowe klasy JMX (com.sun.jdmk w jmxtools.jar)
Group:		Development/Languages/Java
# loose dep to allow using with other JMX implementations (e.g. included in JRE)
Requires:	jmx >= 1.2.1

%description tools
JMX additional classes (com.sun.jdmk in jmxtools.jar).

%description tools -l pl.UTF-8
Dodatkowe klasy JMX (com.sun.jdmk w jmxtools.jar).

%package demo
Summary:	Demo for %{name}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu %{name}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%description demo -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu %{name}.

%prep
%if %{with scsl}
%setup -q -n %{name}-%{fver}-src -T -b1
%patch0 -p1
%else
%setup -q -n %{name}-%{fver}-bin
%endif

%if %{with scsl}
%build
export LC_ALL=en_US # source not in ASCII
%ant
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install %{?with_scsl:build/}lib/jmxri.jar $RPM_BUILD_ROOT%{_javadir}/jmxri-%{version}.jar
install lib/jmxtools.jar $RPM_BUILD_ROOT%{_javadir}/jmxtools-%{version}.jar
ln -s jmxri-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jmxri.jar
ln -s jmxtools-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jmxtools.jar

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -sf %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc doc/{README_SRC.txt,RELEASE_NOTES.txt} LICENSE.html
%{_javadir}/jmxri-%{version}.jar
%{_javadir}/jmxri.jar

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files tools
%defattr(644,root,root,755)
%doc doc/{README_SRC.txt,RELEASE_NOTES.txt} LICENSE.html
%{_javadir}/jmxtools-%{version}.jar
%{_javadir}/jmxtools.jar
