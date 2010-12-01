%define		devstat	Beta1
%define		snap	20101109
Summary:	Hyper's CdCatalog
Summary(hu.UTF-8):	Hyper CD Katalógusa
Summary(pl.UTF-8):	Katalog CDków Hypera
Name:		cdcat
Version:	1.1
Release:	1%{devstat}
License:	GPL
Group:		Applications
Source0:	http://cdcat.sourceforge.net/CdCat-Unicode-1.1%{devstat}-qt4_%{snap}.tar.bz2
# Source0-md5:	adf1294ce6a1507767b09542372fd990
Source1:	%{name}.desktop
Patch0:		%{name}-gcc4.patch
Patch1:		%{name}-fstab.patch
URL:		http://cdcat.sourceforge.net/
BuildRequires:	expat-devel >= 1.95.2
BuildRequires:	pcre-devel >= 1.1.4
BuildRequires:	qt4-qmake
BuildRequires:	qt4-linguist
BuildRequires:	Qt3Support-devel
BuildRequires:	QtGui-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The cdcat is a graphical (Qt based) multiplatform (Linux/Windows)
catalog program which scan your directoryes/drives you want and
memoryze the filesystem /including the tags of MP3's/ and store it a
small file. The database is stored in a gzipped XML format, so you can
hack it, or use it if necessary :-)

%description -l hu.UTF-8
A cdcat egy grafikus (QT alapú) többplatformos (Linux/Windows/MacOS)
katalógus program, mely beolvassa a megadott könyvtárakat és
fájlszerkezeteket, és egy kis fájlban eltárolja, így késõbb könnyedén
visszakereshetők a tárolt programok, zenék, filmek, stb. Az mp3-akhoz
tartozó tag-ek is megjegyzésre kerülnek. Az adatbázis egy gzippelt XML
formátumban tárolódik, így hordozható és könnyen hack-elhetõ, ha kell.

%description -l pl.UTF-8
Cdcat jest graficznym (opartym o Qt) wieloplatformowym (Linux/Windows)
programem katalogującym, który skanuje wybrane dyski i zapamiętuje
system plików (włączając w to znaczniki MP3) i zapisuje to w małym
pliku. Baza danych jest w gzipowanym pliku XML, więc można ją
zmieniać, albo używać w miarę potrzeby.

%prep
%setup -q -n CdCat-Unicode-1.1%{devstat}-qt4_%{snap}
%{__sed} -i "s,lrelease,lrelease-qt4,g" unicode-src/cdcat.pro
# %patch0 -p0
# %patch1 -p0
# echo 'CONFIG += thread' >> src/cdcat.pro

%build
cd unicode-src
export QTDIR=%{_prefix}
qmake-qt4 \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_LINK="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcflags} -fno-exceptions -fno-rtti"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/cdcat/translations

install -D unicode-src/cdcat $RPM_BUILD_ROOT%{_bindir}/cdcat
install unicode-src/lang/cdcat_*.qm $RPM_BUILD_ROOT%{_datadir}/cdcat/translations
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/cdcat.desktop
install -D cdcat.png $RPM_BUILD_ROOT%{_pixmapsdir}/cdcat.png

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Authors README README_IMPORT TRANSLATORS_README TODO VERSION
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/cdcat
%dir %{_datadir}/cdcat/translations
%lang(cs) %{_datadir}/cdcat/translations/cdcat_cz.qm
%lang(de) %{_datadir}/cdcat/translations/cdcat_de.qm
%lang(el) %{_datadir}/cdcat/translations/cdcat_el.qm
%lang(es) %{_datadir}/cdcat/translations/cdcat_es.qm
# %lang(fr) %{_datadir}/cdcat/translations/cdcat_fr.qm
%lang(hu) %{_datadir}/cdcat/translations/cdcat_hu.qm
%lang(id) %{_datadir}/cdcat/translations/cdcat_id.qm
# %lang(it) %{_datadir}/cdcat/translations/cdcat_it.qm
%lang(pl) %{_datadir}/cdcat/translations/cdcat_pl.qm
%lang(pt) %{_datadir}/cdcat/translations/cdcat_pt.qm
%lang(sk) %{_datadir}/cdcat/translations/cdcat_sk.qm
# %lang(sr) %{_datadir}/cdcat/translations/cdcat_sr.qm
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
