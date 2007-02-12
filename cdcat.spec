Summary:	Hyper's CdCatalog
Summary(pl.UTF-8):	Katalog CDków Hypera
Name:		cdcat
Version:	1.01b
Release:	1
License:	GPL
Group:		Applications
Source0:	http://cdcat.sourceforge.net/%{name}-%{version}.tar.bz2
# Source0-md5:	59b321ff3848b34cb6862fd2a408cb44
Source1:	%{name}.desktop
Patch0:		%{name}-gcc4.patch
URL:		http://cdcat.sourceforge.net/
BuildRequires:	expat-devel >= 1.95.2
BuildRequires:	pcre-devel >= 1.1.4
BuildRequires:	qmake
BuildRequires:	qt-devel >= 2.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The cdcat is a graphical (Qt based) multiplatform (Linux/Windows)
catalog program which scan your directoryes/drives you want and
memoryze the filesystem /including the tags of MP3's/ and store it a
small file. The database is stored in a gzipped XML format, so you can
hack it, or use it if necessary :-)

%description -l pl.UTF-8
Cdcat jest graficznym (opartym o Qt) wieloplatformowym (Linux/Windows)
programem katalogującym, który skanuje wybrane dyski i zapamiętuje
system plików (włączając w to znaczniki MP3) i zapisuje to w małym
pliku. Baza danych jest w gzipowanym pliku XML, więc można ją
zmieniać, albo używać w miarę potrzeby.

%prep
%setup -q -n CdCat-%{version}
%patch0 -p0
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
%lang(el) %{_datadir}/cdcat/translations/cdcat_el.qm
%lang(es) %{_datadir}/cdcat/translations/cdcat_es.qm
%lang(fr) %{_datadir}/cdcat/translations/cdcat_fr.qm
%lang(hu) %{_datadir}/cdcat/translations/cdcat_hu.qm
%lang(id) %{_datadir}/cdcat/translations/cdcat_id.qm
%lang(it) %{_datadir}/cdcat/translations/cdcat_it.qm
%lang(pl) %{_datadir}/cdcat/translations/cdcat_pl.qm
%lang(pt) %{_datadir}/cdcat/translations/cdcat_pt.qm
%lang(sk) %{_datadir}/cdcat/translations/cdcat_sk.qm
%lang(sr) %{_datadir}/cdcat/translations/cdcat_sr.qm
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
