Summary:	Hypher's CdCatalog
Summary(pl):	Katalog CDków Hypera
Name:		cdcat
Version:	0.97
Release:	1
License:	GPL
Group:		Applications
Source0:	http://cdcat.sourceforge.net/%{name}-%{version}.tar.bz2
# Source0-md5:	28d3b467301b14185d3173275cf9b854
Source1:	cdcat.desktop
URL:		http://cdcat.sourceforge.net/
BuildRequires:	expat-devel >= 1.95.2
BuildRequires:	pcre-devel >= 1.1.4
BuildRequires:	qt-devel >= 2.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The cdcat is a graphical (QT based) multiplatform (Linux/Windows)
catalog program which scan your directoryes/drives you want and
memoryze the filesystem /including the tags of mp3's/ and store it a
small file.  The database is stored in a gzipped XML format, so you
can hack it, or use it if necessary :-)

%description -l pl
Cdcat jest graficznym (opartym o QT) wieloplatformowym (Linux/Windows)
programem kataloguj±cym, który skanuje wybrane dyski i zapamiêtuje
system plików (w³±czaj±c w to znaczniki mp3) i zapisuje to w ma³ym
pliku. Baza danych jest w gzipowanym pliku XML, wiêc mo¿na j±
zmieniaæ, albo u¿ywaæ w miarê potrzeby.

%prep
%setup -q -n CdCat-%{version}

echo 'CONFIG += thread' >> src/cdcat.pro

%build
cd src
export QTDIR=%{_prefix}
qmake \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_LINK="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcflags} -fno-exceptions -fno-rtti"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/cdcat/translations

install -D src/cdcat $RPM_BUILD_ROOT%{_bindir}/cdcat
install src/lang/cdcat_*.qm $RPM_BUILD_ROOT%{_datadir}/cdcat/translations
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/cdcat.desktop
install -D cdcat.png $RPM_BUILD_ROOT%{_pixmapsdir}/cdcat.png

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Authors ChangeLog README README_IMPORT TRANSLATORS_README TODO VERSION
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/cdcat
%dir %{_datadir}/cdcat/translations
%lang(cs) %{_datadir}/cdcat/translations/cdcat_cz.qm
%lang(de) %{_datadir}/cdcat/translations/cdcat_de.qm
%lang(es) %{_datadir}/cdcat/translations/cdcat_es.qm
%lang(hu) %{_datadir}/cdcat/translations/cdcat_hu.qm
%lang(pl) %{_datadir}/cdcat/translations/cdcat_pl.qm
%{_desktopdir}/*
%{_pixmapsdir}/*
