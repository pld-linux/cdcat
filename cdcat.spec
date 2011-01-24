%define		devstat	beta2
Summary:	Hyper's CdCatalog
Summary(hu.UTF-8):	Hyper CD Katalógusa
Summary(pl.UTF-8):	Katalog CDków Hypera
Name:		cdcat
Version:	1.1
Release:	1%{devstat}
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/project/cdcat/cdcat/cdcat-1.1beta2/%{name}-%{version}%{devstat}.tar.bz2
# Source0-md5:	1d26652cec7b844e0da670a92a181af4
Source1:	%{name}.desktop
Patch0:		%{name}-gcc4.patch
Patch1:		%{name}-fstab.patch
URL:		http://cdcat.sourceforge.net/
BuildRequires:	Qt3Support-devel
BuildRequires:	QtGui-devel
BuildRequires:	expat-devel >= 1.95.2
BuildRequires:	pcre-devel >= 1.1.4
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	qt4-qmake
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
%setup -q -n %{name}-%{version}%{devstat}
%{__sed} -i "s,lrelease,lrelease-qt4,g ;\
	s,/local,,g ;\
	s,\(distfiles.path =\).*,\1 %{_docdir}/%{name}-%{version}," \
	src/cdcat.pro

%build
cd src
export QTDIR=%{_prefix}
qmake-qt4 \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_LINK="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcflags} -fno-exceptions -fno-rtti" \
	cdcat.pro

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd src
%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

install -D ../cdcat.png $RPM_BUILD_ROOT%{_pixmapsdir}/cdcat.png
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/cdcat.desktop

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%docdir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/*
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
