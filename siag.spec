Summary:	Siag Office
Name:		siag
Version:	3.3.11
Release:	1
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	ftp://siag.nu/pub/siag/%{name}-%{version}.tar.bz2
Source1:	gvu.desktop
Source2:	%{name}.desktop
Source3:	xfiler.desktop
Source4:	egon.desktop
Source5:	pw.desktop
Source6:	xedplus.desktop
URL:		http://siag.nu/
Patch0:		%{name}-ref_expander-bug.patch
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
Siag Office jest �ci�le zintegrowanym, darmowym pakietem biurowym.
Sk�ada si� z arkusza kalkulacyjnego Siag, procesora tekst�w PW,
programu do animacji egon, edytora tekstowego XedPlus, mened�era
plik�w Xfiler oraz przegl�darki Gvu.

%package siag
Summary:	Scheme In A Grid - Siag Office spreadsheet
Summary(pl):	Scheme In A Grid - arkusz kalkulacyjny Siag Office
Group:		X11/Applications
Group(pl):	X11/Aplikacje

%description siag
Siag is a spreadsheet based on X and Scheme. It has many, many
features. It contains even webserver! Siag is a part of free Siag
Office package.

Supported file formats: Siag, Comma Separated Values, Plain Text,
Lotus 1-2-3, Postscript, HTML Tables, Scheme Code, Troff Tables, LaTeX
Tables. Additional formats can be supported by using external
converters, such as xls2csv for Microsoft Excel.

%description -l pl siag
Siag jest arkuszem kalkulacyjnym bazuj�cym na systemie Xwindow oraz
j�zyku Scheme. Posiada wiele, bardzo wiele funkcji. Jest wyposa�ony
nawet w serwer WWW! Siag jest cz�ci� pakietu biurowego Siag Office.

Wspierane formaty plik�w: Siag, warto�ci oddzielane przecinkami (Comma
Separated Values), tekst, Lotus 1-2-3, Postscript, tabelki HTML,
�r�d�o Scheme, tabelki Troff oraz Latex. Dodatkowe formaty mog� by�
obs�u�one przy u�yciu zewn�trznych konwerter�w, np. xls2csv dla
Microsoft Excel.

%package pw
Summary:	Pathetic Writer - Siag Office word processor
Summary(pl):	Pathetic Writer - procesor tekst�w Siag Office
Group:		X11/Applications
Group(pl):	X11/Aplikacje

%description pw
Pathetic Writer is an X-based word processor for Unix. It is a part of
free Siag Office package.

Supported file formats: Pathetic Writer, Plain Text, Postscript,
Hypertext Markup Language, Rich Text Format. Some of them require
using external converter called WV.

%description -l pl pw
Pathetic Writer jest procesorem tekst�w bazowanym na systemie X
window. Jest on cz�ci� pakietu biurowego Siag Office.

Wspierane formaty plik�w: Pathetic Writer, tekst, Postscript, HTML,
RTF. Niekt�re z nich w ymagaj� zewn�trznego konwertera o nazwie WV.

%package egon
Summary:	Egon Animator - Siag Office animation software
Summary(pl):	Egon Animator - oprogramowanie do animacji Siag Office
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika

%description egon
Egon Animator is an X-based animation development tool for Unix. The
idea is that "objects" (rectangles, lines, pixmaps and so on) are
added to a "stage" where they are then made to perform by telling them
where they should be and when. Egon Animator is a part of free Siag
Office package.

Supported file formats: Egon Animator, C source, Animated GIF,
Postscript, Text, HTML, Magic Point, MS Powerpoint (pptHtml required).

Sorry but it is currently useless - it segfaults.

%description -l pl egon
Egon Animator jest narz�dziem do tworzenia animacji bazowanym na
systemie X window. Zasada dzia�ania polega na tym, �e "obiekty"
(prostok�ty, linie, obrazki itd.) s� dodawane do "sceny", gdzie
wykonuj� odpowiednie polecenia wskazuj�ce, kiedy i gdzie maj� si�
pojawi�. Egon Animator jest cz�ci� pakietu biurowego Siag Office.

Wspierane formaty plik�w: Egon Animator, �r�d�o w j�zyku C, animowany
GIF, Postscript, tekst, HTML, Magic Point, MS Powerpoint (wymagany
program pptHtml).

Niestety chwilowo program jest bezu�yteczny, gdy� wywo�uje naruszenie
pami�ci.

%package xedplus
Summary:	Siag Office simple but powerful text editor
Summary(pl):	Prosty lecz wydajny edytor tekst�w Siag Office
Group:		X11/Applications/Editors
Group(pl):	X11/Aplikacje/Edytory

%description xedplus
Simple text editor for editing config files or source code. It
contains everything you need including even commands to call sed.
Xedplus is a part of free Siag Office package.

%description -l pl xedplus
Prosty edytor tekst�w do edycji plik�w konfiguracyjnych czy kod�w
�r�d�owych. Posiada wszystko, czego potrzebujesz - nawet komendy, aby
wywo�a� seda. Xedplus jest cz�ci� pakietu biurowego Siag Office.

%package xfiler
Summary:	Siag Office file manager
Summary(pl):	Mened�er plik�w Siag Office
Group:		X11/Utilities
Group(pl):	X11/Narz�dzia

%description xfiler
Simple and easy to use file manager. It contains basic commands to
manage your filesystem. Suits almost all needs of plain user. Xfiler
is a part of free Siag Office package.

%description -l pl xfiler
Prosty i �atwy w u�yciu mened�er plik�w. Posiada podstawowe komendy do
zarz�dzania Twoim systemem plik�w. Wype�nia potrzeby zwyk�ego
u�ytkownika. Xfiler jest cz�ci� pakietu biurowego Siag Office.

%package plugins
Summary:	Plugins to use with Siag Office package
Group:		X11/Applications
Group(pl):	X11/Aplikacje

%description plugins
It contains some plugins for Siag Office package (there are some more
not mentioned here):

- The Image Plugin - It displays most common image formats if the
  NETPBM collection of graphics converters is installed. Otherwise it
  will be able to display XPM images.
- The Dummy Plugin - The dummy application works as a "shim" between
  Siag and another application. It speaks the plugin protocol with Siag
  and does its best to manage the external application.
- The Hello Plugin - This one is for demonstrational purposes only: it
  displays the message "Hello, World" in its window. It is suitable as
  an example of a simple plugin, in that it contains all the necessary
  code to make a plugin of a normal X program.

%description -l pl plugins
Zawiera kilka plugin�w dla pakietu biurowego Siag Office (jest ich
troch� wi�cej ni� opisanych tutaj):

- The Image Plugin - wy�wietla najbardziej popularne formaty plik�w
  je�li jest zainstalowany zestaw konwerter�w NETPBM. W przeciwnym
  wypadku b�dzie wy�wietla� tylko grafik� w formacie XPM.
- The Dummy Plugin - dzia�a jako swoisty interfejst poimi�dzy Siagiem
  a inna aplikacj�. Komunikuje si� protoko�em plugin�w ze Siag i robi,
  co potrafi, aby zarz�dz�� zewn�trzn� aplikacj�.
- The Hello Plugin - stworzony dla cel�w demonstracyjnych: wy�wietla
  komunikat "Hello, World"" w swoim oknie. Jest doskona�ym przyk�adem,
  kt�ry mo�e pos�u�y� do stworzenia w pe�ni dzia�aj�cego pluginu.

%package gvu
Summary:	Siag Office graphics previewer
Summary(pl):	Przegl�darka graficzna Siag Office
Group:		X11/Applications
Group(pl):	X11/Aplikacje

%description gvu
Gvu allows you to easily view Postscript (*.ps) and Encapsulated
Postsript (*.eps) files. It uses Aladdin Ghostscript software to
process files. Gvu is a part of free Siag Office package.

%description -l pl gvu
Gvu umo�liwia �atwe przegl�danie plik�w w formacie Postscript (*.ps)
oraz Encapsulated Postscript (*.eps). Wykorzystuje w tym celu
oprogramowanie Alladin Ghostscript. Gvu jest cz�ci� pakietu biurowego
Siag Office.

%package -n XawM
Summary:	Modified version of X athena widgets in 3d (Xaw3d)
Summary(pl):	Zmodyfikowana wersja tr�jwymiarowych widget�w athena.
Group:		X11/Libraries
Group(pl):	X11/Biblioteki

%description -n XawM
XawM is modified version of X athena widgets in 3d (Xaw3d). It adds 3d
look to applications running under Xwindow.

%description -l pl -n XawM
XawM jest zmodyfikowan� wersj� tr�jowymiarowych widget�w atheny
(Xaw3d). Dodaje "tr�jwymiarowo��" interfejsom aplikacji dzia�aj�cych
pod X window.

%prep
%setup -q 
%patch -p1

%build
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/{Editors,Spreadsheets,Wordprocessors}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install -d $RPM_BUILD_ROOT%{_datadir}/siag/examples/{pw,siag,egon}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Office/Spreadsheets
install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/Graphics
install %{SOURCE5} $RPM_BUILD_ROOT%{_applnkdir}/Office/Wordprocessors
install %{SOURCE6} $RPM_BUILD_ROOT%{_applnkdir}/Office/Editors

install pw/examples/*.{doc,pw,html,rtf,txt,bmk} $RPM_BUILD_ROOT%{_datadir}/siag/examples/pw
install siag/examples/*.{wk1,siag,csv} $RPM_BUILD_ROOT%{_datadir}/siag/examples/siag
install egon/examples/*.egon $RPM_BUILD_ROOT%{_datadir}/siag/examples/egon

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
%{_datadir}/siag/common/bitmaps/SO3.xpm
%{_datadir}/siag/common/bitmaps/back.xpm
%{_datadir}/siag/common/bitmaps/blank.xpm
%{_datadir}/siag/common/bitmaps/bold.xpm
%{_datadir}/siag/common/bitmaps/book-closed.xpm
%{_datadir}/siag/common/bitmaps/book-open.xpm
%{_datadir}/siag/common/bitmaps/borders.xpm
%{_datadir}/siag/common/bitmaps/cancel.xpm
%{_datadir}/siag/common/bitmaps/center.xpm
%{_datadir}/siag/common/bitmaps/compress.xpm
%{_datadir}/siag/common/bitmaps/copy.xpm
%{_datadir}/siag/common/bitmaps/copyright.xpm
%{_datadir}/siag/common/bitmaps/cut.xpm
%{_datadir}/siag/common/bitmaps/data.xpm
%{_datadir}/siag/common/bitmaps/editor.xpm
%{_datadir}/siag/common/bitmaps/fld_closed.xpm
%{_datadir}/siag/common/bitmaps/fld_new.xpm
%{_datadir}/siag/common/bitmaps/fld_open.xpm
%{_datadir}/siag/common/bitmaps/fld_up.xpm
%{_datadir}/siag/common/bitmaps/fonts.xpm
%{_datadir}/siag/common/bitmaps/ghost.xpm
%{_datadir}/siag/common/bitmaps/grid.xpm
%{_datadir}/siag/common/bitmaps/handlebg.xpm
%{_datadir}/siag/common/bitmaps/hcenter.xpm
%{_datadir}/siag/common/bitmaps/hleft.xpm
%{_datadir}/siag/common/bitmaps/home.xpm
%{_datadir}/siag/common/bitmaps/hright.xpm
%{_datadir}/siag/common/bitmaps/icons.xpm
%{_datadir}/siag/common/bitmaps/image.xpm
%{_datadir}/siag/common/bitmaps/info.xpm
%{_datadir}/siag/common/bitmaps/insert.xpm
%{_datadir}/siag/common/bitmaps/italic.xpm
%{_datadir}/siag/common/bitmaps/landscape.xpm
%{_datadir}/siag/common/bitmaps/larger.xpm
%{_datadir}/siag/common/bitmaps/lline.xpm
%{_datadir}/siag/common/bitmaps/netscape.xpm
%{_datadir}/siag/common/bitmaps/new.xpm
%{_datadir}/siag/common/bitmaps/next.xpm
%{_datadir}/siag/common/bitmaps/none.xpm
%{_datadir}/siag/common/bitmaps/overwrite.xpm
%{_datadir}/siag/common/bitmaps/paste.xpm
%{_datadir}/siag/common/bitmaps/play.xpm
%{_datadir}/siag/common/bitmaps/plotter.xpm
%{_datadir}/siag/common/bitmaps/portrait.xpm
%{_datadir}/siag/common/bitmaps/preview.xpm
%{_datadir}/siag/common/bitmaps/previous.xpm
%{_datadir}/siag/common/bitmaps/printer.xpm
%{_datadir}/siag/common/bitmaps/quit.xpm
%{_datadir}/siag/common/bitmaps/redo.xpm
%{_datadir}/siag/common/bitmaps/reload.xpm
%{_datadir}/siag/common/bitmaps/rline.xpm
%{_datadir}/siag/common/bitmaps/save.xpm
%{_datadir}/siag/common/bitmaps/search.xpm
%{_datadir}/siag/common/bitmaps/siagoffice.xpm
%{_datadir}/siag/common/bitmaps/sigma.xpm
%{_datadir}/siag/common/bitmaps/smaller.xpm
%{_datadir}/siag/common/bitmaps/sortaz.xpm
%{_datadir}/siag/common/bitmaps/sortmode.xpm
%{_datadir}/siag/common/bitmaps/sortza.xpm
%{_datadir}/siag/common/bitmaps/spell.xpm
%{_datadir}/siag/common/bitmaps/stop.xpm
%{_datadir}/siag/common/bitmaps/uchar.xpm
%{_datadir}/siag/common/bitmaps/uline.xpm
%{_datadir}/siag/common/bitmaps/undo.xpm
%{_datadir}/siag/common/bitmaps/unknown.xpm
%{_datadir}/siag/common/bitmaps/vbottom.xpm
%{_datadir}/siag/common/bitmaps/viewmode.xpm
%{_datadir}/siag/common/bitmaps/vtop.xpm
%{_datadir}/siag/common/bitmaps/xterm16.xpm
%{_datadir}/siag/common/bitmaps/kde/back.xpm
%{_datadir}/siag/common/bitmaps/kde/cancel.xpm
%{_datadir}/siag/common/bitmaps/kde/copy.xpm
%{_datadir}/siag/common/bitmaps/kde/cut.xpm
%{_datadir}/siag/common/bitmaps/kde/fld_open.xpm
%{_datadir}/siag/common/bitmaps/kde/forward.xpm
%{_datadir}/siag/common/bitmaps/kde/home.xpm
%{_datadir}/siag/common/bitmaps/kde/info.xpm
%{_datadir}/siag/common/bitmaps/kde/larger.xpm
%{_datadir}/siag/common/bitmaps/kde/new.xpm
%{_datadir}/siag/common/bitmaps/kde/next.xpm
%{_datadir}/siag/common/bitmaps/kde/paste.xpm
%{_datadir}/siag/common/bitmaps/kde/play.xpm
%{_datadir}/siag/common/bitmaps/kde/preview.xpm
%{_datadir}/siag/common/bitmaps/kde/previous.xpm
%{_datadir}/siag/common/bitmaps/kde/printer.xpm
%{_datadir}/siag/common/bitmaps/kde/quit.xpm
%{_datadir}/siag/common/bitmaps/kde/reload.xpm
%{_datadir}/siag/common/bitmaps/kde/save.xpm
%{_datadir}/siag/common/bitmaps/kde/saveas.xpm
%{_datadir}/siag/common/bitmaps/kde/search.xpm
%{_datadir}/siag/common/bitmaps/kde/smaller.xpm
%{_datadir}/siag/common/bitmaps/kde/stop.xpm
%{_datadir}/siag/common/bitmaps/gnome/back.xpm
%{_datadir}/siag/common/bitmaps/gnome/bold.xpm
%{_datadir}/siag/common/bitmaps/gnome/cancel.xpm
%{_datadir}/siag/common/bitmaps/gnome/copy.xpm
%{_datadir}/siag/common/bitmaps/gnome/cut.xpm
%{_datadir}/siag/common/bitmaps/gnome/fld_open.xpm
%{_datadir}/siag/common/bitmaps/gnome/forward.xpm
%{_datadir}/siag/common/bitmaps/gnome/hcenter.xpm
%{_datadir}/siag/common/bitmaps/gnome/hleft.xpm
%{_datadir}/siag/common/bitmaps/gnome/home.xpm
%{_datadir}/siag/common/bitmaps/gnome/hright.xpm
%{_datadir}/siag/common/bitmaps/gnome/info.xpm
%{_datadir}/siag/common/bitmaps/gnome/italic.xpm
%{_datadir}/siag/common/bitmaps/gnome/new.xpm
%{_datadir}/siag/common/bitmaps/gnome/next.xpm
%{_datadir}/siag/common/bitmaps/gnome/paste.xpm
%{_datadir}/siag/common/bitmaps/gnome/play.xpm
%{_datadir}/siag/common/bitmaps/gnome/previous.xpm
%{_datadir}/siag/common/bitmaps/gnome/printer.xpm
%{_datadir}/siag/common/bitmaps/gnome/quit.xpm
%{_datadir}/siag/common/bitmaps/gnome/redo.xpm
%{_datadir}/siag/common/bitmaps/gnome/reload.xpm
%{_datadir}/siag/common/bitmaps/gnome/save.xpm
%{_datadir}/siag/common/bitmaps/gnome/saveas.xpm
%{_datadir}/siag/common/bitmaps/gnome/search.xpm
%{_datadir}/siag/common/bitmaps/gnome/spell.xpm
%{_datadir}/siag/common/bitmaps/gnome/stop.xpm
%{_datadir}/siag/common/bitmaps/gnome/uchar.xpm
%{_datadir}/siag/common/bitmaps/gnome/undo.xpm
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
%{_datadir}/siag/common/bitmaps/siag.xpm
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
%{_datadir}/siag/examples/siag/*
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
%{_datadir}/siag/common/bitmaps/pw.xpm
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
%{_datadir}/siag/examples/pw/*
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
%{_datadir}/siag/common/bitmaps/egon.xpm
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
%{_datadir}/siag/examples/egon/*
%{_mandir}/man1/egon.1*
%{_applnkdir}/Graphics/egon.desktop

%files xedplus
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xedplus
%{_datadir}/siag/common/bitmaps/xedplus.xpm
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
%{_datadir}/siag/common/bitmaps/xfiler.xpm
%doc xfiler/README.gz
%doc xfiler/TODO.gz
%doc xfiler/xfiler.html.gz
%{_mandir}/man1/xfiler.1*
%{_applnkdir}/Utilities/xfiler.desktop
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
%{_datadir}/siag/common/bitmaps/gvu.xpm
%doc gvu/README.gz
%doc gvu/TODO.gz
%{_mandir}/man1/gvu.1*
%{_applnkdir}/Graphics/Viewers/gvu.desktop

%files -n XawM
%defattr(644,root,root,755)
%{_libdir}/libXawM.so.*.*
%doc XawM/README.gz
%doc XawM/README.Linux.gz
%doc XawM/README.XAW3D.gz
%doc XawM/README.XawM.gz
