Summary:	Hyper's CdCatalog
Summary(hu.UTF-8):	Hyper CD Katalógusa
Summary(pl.UTF-8):	Katalog CDków Hypera
Name:		cdcat
Version:	2.3.1
Release:	3
Epoch:		1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/cdcat/%{name}-%{version}.tar.bz2
# Source0-md5:	b7b4ea3e213620c1126c64125b93e63a
Source1:	%{name}.desktop
Patch0:		cryptopp.patch
URL:		http://cdcat.sourceforge.net/
BuildRequires:	Qt3Support-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	QtXml-devel >= 4
BuildRequires:	expat-devel >= 1.95.2
BuildRequires:	cryptopp-devel
BuildRequires:	libmediainfo-devel
BuildRequires:	libtar-devel
BuildRequires:	lib7zip-devel >= 1.6.5-2
BuildRequires:	pcre-devel >= 1.1.4
BuildRequires:	qt4-build >= 4
BuildRequires:	qt4-linguist >= 4
BuildRequires:	qt4-qmake >= 4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The cdcat is a graphical (Qt based) multiplatform (Linux/Windows)
catalog program which scans your directories/drives you want and
memorizes the filesystem (including the tags of MP3s) and stores it in
a small file. The database is stored in a gzipped XML format, so you
can hack it, or use it if necessary :-)

%description -l hu.UTF-8
A cdcat egy grafikus (QT alapú) többplatformos (Linux/Windows/MacOS)
katalógus program, mely beolvassa a megadott könyvtárakat és
fájlszerkezeteket, és egy kis fájlban eltárolja, így késõbb könnyedén
visszakereshetők a tárolt programok, zenék, filmek, stb. Az mp3-akhoz
tartozó tag-ek is megjegyzésre kerülnek. Az adatbázis egy gzippelt XML
formátumban tárolódik, így hordozható és könnyen hack-elhetõ, ha kell.

%description -l pl.UTF-8
Cdcat jest graficznym (opartym o Qt) wieloplatformowym (Linux/Windows)
programem katalogującym, który skanuje wybrane katalogi/urządzenia,
zapamiętuje system plików (wraz ze znacznikami MP3) i zapisuje to w
małym pliku. Baza danych jest w gzipowanym pliku XML, więc można ją
zmieniać, albo używać w miarę potrzeby.

%prep
%setup -q -n %{name}-%{version}
%patch -P0 -p1
%{__sed} -i "s,lrelease,lrelease-qt4,g ;\
	s,/usr/local,/usr,g ;\
	s,\(distfiles.path =\).*,\1 %{_docdir}/%{name}-%{version}," \
	src/cdcat.pro
%{__sed} -i "s@\.\./COPYING@../README_IMPORT ../README_IMPORT.DE ../README_IMPORT.HU@" src/cdcat.pro

%build
cd src
export QTDIR=%{_prefix}
qmake-qt4 \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_LINK="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcflags}" \
	cdcat.pro

%{__make}

cd lang
lrelease-qt4 *.ts

%install
rm -rf $RPM_BUILD_ROOT
cd src
%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

install -D ../cdcat.png $RPM_BUILD_ROOT%{_pixmapsdir}/cdcat.png
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/cdcat.desktop
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/translations
install lang/*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/translations

%{__rm} -f $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/cdcat
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
%lang(ru) %{_datadir}/cdcat/translations/cdcat_ru.qm
%lang(sk) %{_datadir}/cdcat/translations/cdcat_sk.qm
%lang(sr) %{_datadir}/cdcat/translations/cdcat_sr.qm
%{_desktopdir}/cdcat.desktop
%{_pixmapsdir}/cdcat.png
