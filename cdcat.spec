Summary:	Hypher's CdCatalog
Summary(pl):	Katalog CDków Hypera
Name:		cdcat
Version:	0.93
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/cdcat/cdcat-0.93.tar.bz2
# Source0-md5:	5d27a6f7cf8f887dadbf2cb5caa16e24
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
system plików, w³±czaj±c w to znaczniki mp3, i zapisuje to w ma³ym
pliku. Baza danych jest w gzipowanym pliku XML, wiêc mo¿esz j±
zmieniaæ, albo u¿ywaæ w miarê potrzeby. 

%prep
%setup -n CdCat-%{version}

%build
cd src
export QTDIR=%{_prefix}
export QMAKESPEC="%{_datadir}/qt/mkspecs/linux-g++/"
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D src/cdcat $RPM_BUILD_ROOT%{_bindir}/cdcat
for L in de es cz hu; do
	install -D src/lang/cdcat_$L.qm $RPM_BUILD_ROOT%{_datadir}/cdcat/translations/cdcat_$L.qm
done
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/cdcat.desktop
install -D cdcat.png $RPM_BUILD_ROOT%{_pixmapsdir}/cdcat.png

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Authors ChangeLog README README_CSV_IMPORT TRANSLATORS_README TODO VERSION
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_datadir}/cdcat
