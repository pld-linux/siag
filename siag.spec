Summary:	Siag Office
Name:		siag
Version:	3.3.11
Release:	0
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	ftp://siag.nu/pub/siag/%{name}-%{version}.tar.bz2
Source1:	gvu.desktop
Source2:	siag.desktop
Source3:	xfiler.desktop
Source4:	egon.desktop
Source5:	pw.desktop
Source6:	xedplus.desktop
URL:		http://siag.nu/
Patch0:		siag-ref_expander-bug.patch
#BuildRequires:	tcl-devel
#BuildRequires:	python-devel
BuildRequires:	XFree86-devel
BuildRequires:	bzip2-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Siag Office is a tightly integrated, free office package. It consists
of the spreadsheet Siag, the word processor PW, the animation program
Egon, the text editor XedPlus, the file manager Xfiler and the
previewer Gvu.

Install this package if you want to use any of Siag Office programs.

%description -l pl
Siag Office jest ¶ci¶le zintegrowanym, darmowym pakietem biurowym. Sk³ada siê
z arkusza kalkulacyjnego Siag, procesora tekstów PW, programu do animacji
egon, edytora tekstowego XedPlus, mened¿era plików Xfiler oraz przegl±darki
Gvu.

%package siag
Summary:	Scheme In A Grid - Siag Office spreadsheet
Summary(pl):	Scheme In A Grid - arkusz kalkulacyjny Siag Office
Group:		X11/Applications
Group(pl):	X11/Aplikacje

%description siag
Siag is a spreadsheet based on X and Scheme. It has many, many
features. It contains even webserver! Siag is a part of free Siag Office
package.

Supported file formats: Siag, Comma Separated Values, Plain Text,
Lotus 1-2-3, Postscript, HTML Tables, Scheme Code, Troff Tables, LaTeX
Tables. Additional formats can be supported by using external
converters, such as xls2csv for Microsoft Excel.

%description -l pl siag
Siag jest arkuszem kalkulacyjnym bazuj±cym na systemie Xwindow oraz jêzyku
Scheme. Posiada wiele, bardzo wiele funkcji. Jest wyposa¿ony nawet w serwer
WWW! Siag jest czê¶ci± pakietu biurowego Siag Office.

Wspierane formaty plików: Siag, warto¶ci oddzielane przecinkami (Comma
Separated Values), tekst, Lotus 1-2-3, Postscript, tabelki HTML, ¼ród³o
Scheme, tabelki Troff oraz Latex. Dodatkowe formaty mog± byæ obs³u¿one przy
u¿yciu zewnêtrznych konwerterów, np. xls2csv dla Microsoft Excel.

%package pw
Summary:	Pathetic Writer - Siag Office word processor
Summary(pl):	Pathetic Writer - procesor tekstów Siag Office
Group:		X11/Applications
Group(pl):	X11/Aplikacje

%description pw
Pathetic Writer is an X-based word processor for Unix. It is a part of
free Siag Office package.

Supported file formats: Pathetic Writer, Plain Text, Postscript,
Hypertext Markup Language, Rich Text Format. Some of them require
using external converter called WV.

%description -l pl pw
Pathetic Writer jest procesorem tekstów bazowanym na systemie X window. Jest
on czê¶ci± pakietu biurowego Siag Office.

Wspierane formaty plików: Pathetic Writer, tekst, Postscript, HTML, RTF.
Niektóre z nich w ymagaj± zewnêtrznego konwertera o nazwie WV.

%package egon
Summary:	Egon Animator - Siag Office animation software
Summary(pl):	Egon Animator - oprogramowanie do animacji Siag Office
Group:		X11/Applications
Group(pl):	X11/Aplikacje

%description egon
Egon Animator is an X-based animation development tool for Unix. The
idea is that "objects" (rectangles, lines, pixmaps and so on) are
added to a "stage" where they are then made to perform by telling them
where they should be and when. Egon Animator is a part of free Siag Office
package.

Supported file formats: Egon Animator, C source, Animated GIF,
Postscript, Text, HTML, Magic Point, MS Powerpoint (pptHtml required).

Sorry but it is currently useless - it segfaults.

%description -l pl egon
Egon Animator jest narzêdziem do tworzenia animacji bazowanym na systemie
X window. Zasada dzia³ania polega na tym, ¿e "obiekty" (prostok±ty, linie,
obrazki itd.) s± dodawane do "sceny", gdzie wykonuj± odpowiednie polecenia
wskazuj±ce, kiedy i gdzie maj± siê pojawiæ. Egon Animator jest czê¶ci± pakietu
biurowego Siag Office.

Wspierane formaty plików: Egon Animator, ¼ród³o w jêzyku C, animowany GIF,
Postscript, tekst, HTML, Magic Point, MS Powerpoint (wymagany program pptHtml).

Niestety chwilowo program jest bezu¿yteczny, gdy¿ wywo³uje naruszenie pamiêci.

%package xedplus
Summary:	Siag Office simple but powerful text editor
Summary(pl):	Prosty lecz wydajny edytor tekstów Siag Office
Group:		X11/Applications
Group(pl):	X11/Aplikacje

%description xedplus
Simple text editor for editing config files or source code. It
contains everything you need including even commands to call sed. Xedplus
is a part of free Siag Office package.

%description -l pl xedplus
Prosty edytor tekstów do edycji plików konfiguracyjnych czy kodów ¼ród³owych.
Posiada wszystko, czego potrzebujesz - nawet komendy, aby wywo³aæ seda.
Xedplus jest czê¶ci± pakietu biurowego Siag Office.

%package xfiler
Summary:	Siag Office file manager
Summary(pl):	Mened¿er plików Siag Office
Group:		X11/Applications
Group(pl):	X11/Aplikacje

%description xfiler
Simple and easy to use file manager. It contains basic commands to
manage your filesystem. Suits almost all needs of plain user. Xfiler is a
part of free Siag Office package.

%description -l pl xfiler
Prosty i ³atwy w u¿yciu mened¿er plików. Posiada podstawowe komendy do
zarz±dzania Twoim systemem plików. Wype³nia potrzeby zwyk³ego u¿ytkownika.
Xfiler jest czê¶ci± pakietu biurowego Siag Office.

%package plugins
Summary:	Plugins to use with Siag Office package
Group:		X11/Applications
Group(pl):	X11/Aplikacje

%description plugins
It contains some plugins for Siag Office package (there are some more
not mentioned here):

- The Image Plugin - It displays most common image formats if the NETPBM
  collection of graphics converters is installed. Otherwise it will be
  able to display XPM images.
- The Dummy Plugin - The dummy application works as a "shim" between
  Siag and another application. It speaks the plugin protocol with Siag
  and does its best to manage the external application.
- The Hello Plugin - This one is for demonstrational purposes only: it
  displays the message "Hello, World" in its window. It is suitable as
  an example of a simple plugin, in that it contains all the necessary
  code to make a plugin of a normal X program.

%description -l pl plugins
Zawiera kilka pluginów dla pakietu biurowego Siag Office (jest ich trochê
wiêcej ni¿ opisanych tutaj):

- The Image Plugin - wy¶wietla najbardziej popularne formaty plików je¶li
  jest zainstalowany zestaw konwerterów NETPBM. W przeciwnym wypadku bêdzie
  wy¶wietla³ tylko grafikê w formacie XPM.
- The Dummy Plugin - dzia³a jako swoisty interfejst poimiêdzy Siagiem 
  a inna aplikacj±. Komunikuje siê protoko³em pluginów ze Siag i robi, co
  potrafi, aby zarz±dz±æ zewnêtrzn± aplikacj±.
- The Hello Plugin - stworzony dla celów demonstracyjnych: wy¶wietla komunikat
  "Hello, World"" w swoim oknie. Jest doskona³ym przyk³adem, który mo¿e
  pos³u¿yæ do stworzenia w pe³ni dzia³aj±cego pluginu.

%package gvu
Summary:	Siag Office graphics previewer
Summary(pl):	Przegl±darka graficzna Siag Office
Group:		X11/Applications
Group(pl):	X11/Aplikacje

%description gvu
Gvu allows you to easily view Postscript (*.ps) and Encapsulated
Postsript (*.eps) files. It uses Aladdin Ghostscript software to
process files. Gvu is a part of free Siag Office package.

%description -l pl gvu
Gvu umo¿liwia ³atwe przegl±danie plików w formacie Postscript (*.ps) oraz
Encapsulated Postscript (*.eps). Wykorzystuje w tym celu oprogramowanie
Alladin Ghostscript. Gvu jest czê¶ci± pakietu biurowego Siag Office.

%package -n XawM
Summary:	Modified version of X athena widgets in 3d (Xaw3d)
Summary(pl):	Zmodyfikowana wersja trójwymiarowych widgetów athena.
Group:		X11/Libraries
Group(pl):	X11/Biblioteki

%description -n XawM
XawM is modified version of X athena widgets in 3d (Xaw3d). It adds 3d
look to applications running under Xwindow.

%description -l pl -n XawM
XawM jest zmodyfikowan± wersj± trójowymiarowych widgetów atheny (Xaw3d).
Dodaje "trójwymiarowo¶æ" interfejsom aplikacji dzia³aj±cych pod X window.

%prep
%setup -q 
%patch -p1

%build
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/{Editors,Misc,Spreadsheets,Wordprocessors}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Office/Misc
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Office/Spreadsheets
install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Office/Misc
install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/Office/Misc
install %{SOURCE5} $RPM_BUILD_ROOT%{_applnkdir}/Office/Wordprocessors
install %{SOURCE6} $RPM_BUILD_ROOT%{_applnkdir}/Office/Editors


gzip -9nf AUTHORS ChangeLog FILES NEWS NLS README \
          {common,xcommon,siag,pw,egon,siod}/docs/* \
	  xed/{README,TODO,xedplus.html} \
          xfiler/{README,TODO,xfiler.html} plugins/{README,TODO} \
	  gvu/{README,TODO} XawM/README{,.Linux,.XAW3D,.XawM} \
	  $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n XawM -p /sbin/ldconfig
%postun -n XawM -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mgptotxt
%attr(755,root,root) %{_bindir}/siaghelp
%attr(755,root,root) %{_bindir}/siagrun
%{_datadir}/siag/common/FontDataBase
%{_datadir}/siag/common/IsoLatin1.enc
%{_datadir}/siag/common/IsoLatin2.enc
%attr(755,root,root) %{_datadir}/siag/common/any2xpm
%{_datadir}/siag/common/common.scm
#here should be something with lang or not?
%{_datadir}/siag/common/dictionary.*
%{_datadir}/siag/common/fonts.txt
%{_datadir}/siag/common/position.scm
%attr(755,root,root) %{_datadir}/siag/common/readpfa
%{_datadir}/siag/common/rgb.txt
%{_datadir}/siag/common/t1lib.config
%{_datadir}/siag/common/tools.scm
%{_datadir}/siag/common/bitmaps/*
%{_datadir}/siag/siod/siod.scm
%{_datadir}/siag/xcommon/StringDefs.scm
%{_datadir}/siag/xcommon/form.scm
#FILES need patching
%doc AUTHORS.gz ChangeLog.gz FILES.gz NEWS.gz NLS.gz README.gz
%doc common/docs/Copyright.gz
%doc common/docs/credits.html.gz
%doc common/docs/embedding.html.gz
%doc common/docs/form.html.gz
%doc common/docs/interpreters.html.gz
%doc common/docs/office.html.gz
%doc common/docs/plugins.html.gz
%doc common/docs/search.html.gz
%doc common/docs/siaghelp.html.gz
%doc xcommon/docs/TODO.gz
%doc siod/docs/siod.html.gz
%{_mandir}/man1/siod.1*

%files siag
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/siag
%attr(755,root,root) %{_bindir}/tsiag
%{_datadir}/siag/siag/123.scm
%{_datadir}/siag/siag/data.scm
%{_datadir}/siag/siag/external.load
%{_datadir}/siag/siag/external.save
%{_datadir}/siag/siag/filemgr.scm
%{_datadir}/siag/siag/find.scm
%{_datadir}/siag/siag/keytable.scm
%{_datadir}/siag/siag/mailto.scm
%{_datadir}/siag/siag/menu.scm
%{_datadir}/siag/siag/plot.scm
%{_datadir}/siag/siag/siag-http.scm
%{_datadir}/siag/siag/siag-net.scm
%{_datadir}/siag/siag/siag.scm
%{_datadir}/siag/siag/sort.scm
%{_datadir}/siag/siag/splot.scm
%{_datadir}/siag/siag/styles.scm
%{_datadir}/siag/siag/toolbar.scm
%{_datadir}/siag/siag/usermgr.scm
%doc siag/docs/BUGS.gz
%doc siag/docs/README.gz
%doc siag/docs/TODO.gz
%doc siag/docs/c-expr.html.gz
%doc siag/docs/commands.html.gz
%doc siag/docs/concepts.html.gz
%doc siag/docs/fileformats.html.gz
%doc siag/docs/form.html.gz
%doc siag/docs/gnuplot.html.gz
%doc siag/docs/intro.html.gz
%doc siag/docs/invocation.html.gz
%doc siag/docs/keys.html.gz
%doc siag/docs/mouse.html.gz
%doc siag/docs/scheme.html.gz
%doc siag/docs/scrollbars.html.gz
%doc siag/docs/siag.gif.gz
%doc siag/docs/siag.html.gz
%doc siag/docs/strings.html.gz
#%doc siag/examples/*
%{_mandir}/man1/siag.1*
%{_applnkdir}/Office/Spreadsheets/siag.desktop

%files pw
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pw
%{_datadir}/siag/pw/external.load
%{_datadir}/siag/pw/external.save
%{_datadir}/siag/pw/menu.scm
%{_datadir}/siag/pw/pw.scm
%{_datadir}/siag/pw/styles.scm
%doc pw/docs/BUGS.gz
%doc pw/docs/TODO.gz
%doc pw/docs/commands.html.gz
%doc pw/docs/concepts.html.gz
%doc pw/docs/fileformats.html.gz
%doc pw/docs/intro.html.gz
%doc pw/docs/invocation.html.gz
%doc pw/docs/keys.html.gz
%doc pw/docs/mouse.html.gz
%doc pw/docs/pw.gif.gz
%doc pw/docs/pw.html.gz
%doc pw/docs/scheme.html.gz
%doc pw/docs/scrollbars.html.gz
%doc pw/docs/spell.html.gz
%doc pw/docs/strings.html.gz
%doc pw/docs/toolbar.html.gz
#%doc pw/examples/*
%{_mandir}/man1/pw.1*
%{_applnkdir}/Office/Wordprocessors/pw.desktop

%files egon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/egon
%{_datadir}/siag/egon/animator.scm
%{_datadir}/siag/egon/egon.scm
%{_datadir}/siag/egon/external.load
%{_datadir}/siag/egon/external.save
%{_datadir}/siag/egon/menu.scm
%doc egon/docs/BUGS.gz
%doc egon/docs/TODO.gz
%doc egon/docs/commands.html.gz
%doc egon/docs/concepts.html.gz
%doc egon/docs/egon.gif.gz
%doc egon/docs/egon.html.gz
%doc egon/docs/fileformats.html.gz
%doc egon/docs/intro.html.gz
%doc egon/docs/invocation.html.gz
%doc egon/docs/keys.html.gz
%doc egon/docs/mouse.html.gz
%doc egon/docs/scheme.html.gz
%doc egon/docs/scrollbars.html.gz
%doc egon/docs/strings.html.gz
%doc egon/docs/toolbar.html.gz
#%doc egon/examples/*
%{_mandir}/man1/egon.1*
%{_applnkdir}/Office/Misc/egon.desktop

%files xedplus
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xedplus
%doc xed/README.gz
%doc xed/TODO.gz
%doc xed/xedplus.html.gz
%{_mandir}/man1/xedplus.1*
%{_applnkdir}/Office/Editors/xedplus.desktop

%files xfiler
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xfiler
%attr(755,root,root) %{_bindir}/runcmd
%{_datadir}/siag/xfiler/FilesMagic
%{_datadir}/siag/xfiler/Filesrc
%attr(755,root,root) %{_datadir}/siag/xfiler/makeicons
%doc xfiler/README.gz
%doc xfiler/TODO.gz
%doc xfiler/xfiler.html.gz
%{_mandir}/man1/xfiler.1*
%{_applnkdir}/Office/Misc/xfiler.desktop
#BITMAPS MISSING!!!

%files plugins
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}exec/siag/plugins/clipart
%attr(755,root,root) %{_libdir}exec/siag/plugins/dummy
%attr(755,root,root) %{_libdir}exec/siag/plugins/form
%attr(755,root,root) %{_libdir}exec/siag/plugins/hello
%attr(755,root,root) %{_libdir}exec/siag/plugins/image
%attr(755,root,root) %{_libdir}exec/siag/plugins/plot
%attr(755,root,root) %{_libdir}exec/siag/plugins/text
%doc plugins/README.gz
%doc plugins/TODO.gz
%{_datadir}/siag/plugins/dummy.scm
%{_datadir}/siag/plugins/plugin.scm
%{_mandir}/man1/dummy_plugin.1*

%files gvu
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvu
%doc gvu/README.gz
%doc gvu/TODO.gz
%{_mandir}/man1/gvu.1*
%{_applnkdir}/Office/Misc/gvu.desktop

%files -n XawM
%defattr(644,root,root,755)
%{_libdir}/libXawM.so.*.*
%doc XawM/README.gz
%doc XawM/README.Linux.gz
%doc XawM/README.XAW3D.gz
%doc XawM/README.XawM.gz
