Summary:	Siag Office
Summary(pl):	Pakiet biurowy Siag Office
Name:		siag
Version:	3.5.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://siag.nu/pub/siag/%{name}-%{version}.tar.gz
# Source0-md5:	68952a28b9be117e2072e9e2e1e43fce
Source1:	gvu.desktop
Source2:	%{name}.desktop
Source3:	xfiler.desktop
Source4:	egon.desktop
Source5:	pw.desktop
Source6:	xedplus.desktop
Source7:	gvu.png
Source8:	%{name}.png
Source9:	xfiler.png
Source10:	egon.png
Source11:	pw.png
Source12:	xedplus.png
URL:		http://siag.nu/
BuildRequires:	XFree86-devel
BuildRequires:	bzip2-devel
BuildRequires:	freetype1-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	ncurses-devel
#BuildRequires:	python-devel
#BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Siag Office is a tightly integrated, fast and free office package. It
consists of the spreadsheet Siag, the word processor PW, the animation
program Egon, the text editor XedPlus, the file manager Xfiler and the
previewer Gvu.

Install this package if you want to use any of Siag Office programs.

%description -l pl
Siag Office jest ¶ci¶le zintegrowanym, szybkim darmowym pakietem
biurowym. Sk³ada siê z arkusza kalkulacyjnego Siag, procesora tekstów
PW, programu do animacji egon, edytora tekstowego XedPlus, zarz±dcy
plików Xfiler oraz przegl±darki Gvu.

%package siag
Summary:	Scheme In A Grid - Siag Office spreadsheet
Summary(pl):	Scheme In A Grid - arkusz kalkulacyjny Siag Office
Group:		X11/Applications
Requires:	%{name} = %{version}

%description siag
Siag is a spreadsheet based on X and Scheme. It has many, many
features. It contains even webserver! Siag is a part of free Siag
Office package.

Supported file formats: Siag, Comma Separated Values, Plain Text,
Lotus 1-2-3, Postscript, HTML Tables, Scheme Code, Troff Tables, LaTeX
Tables. Additional formats can be supported by using external
converters, such as xls2csv for Microsoft Excel.

%description siag -l pl
Siag jest arkuszem kalkulacyjnym bazuj±cym na systemie X Window oraz
jêzyku Scheme. Posiada wiele, bardzo wiele funkcji. Jest wyposa¿ony
nawet w serwer WWW! Siag jest czê¶ci± pakietu biurowego Siag Office.

Wspierane formaty plików: Siag, warto¶ci oddzielane przecinkami (Comma
Separated Values), tekst, Lotus 1-2-3, Postscript, tabelki HTML,
¼ród³o Scheme, tabelki Troff oraz Latex. Dodatkowe formaty mog± byæ
obs³u¿one przy u¿yciu zewnêtrznych konwerterów, np. xls2csv dla
Microsoft Excel.

%package pw
Summary:	Pathetic Writer - Siag Office word processor
Summary(pl):	Pathetic Writer - procesor tekstów Siag Office
Group:		X11/Applications
Requires:	%{name} = %{version}

%description pw
Pathetic Writer is an X-based word processor for Unix. It is a part of
free Siag Office package.

Supported file formats: Pathetic Writer, Plain Text, Postscript,
Hypertext Markup Language, Rich Text Format. Some of them require
using external converter called WV.

%description pw -l pl
Pathetic Writer jest procesorem tekstów bazowanym na systemie X
Window. Jest on czê¶ci± pakietu biurowego Siag Office.

Wspierane formaty plików: Pathetic Writer, tekst, Postscript, HTML,
RTF. Niektóre z nich wymagaj± zewnêtrznego konwertera o nazwie WV.

%package egon
Summary:	Egon Animator - Siag Office animation software
Summary(pl):	Egon Animator - oprogramowanie do animacji Siag Office
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description egon
Egon Animator is an X-based animation development tool for Unix. The
idea is that "objects" (rectangles, lines, pixmaps and so on) are
added to a "stage" where they are then made to perform by telling them
where they should be and when. Egon Animator is a part of free Siag
Office package.

Supported file formats: Egon Animator, C source, Animated GIF,
Postscript, Text, HTML, Magic Point, MS Powerpoint (pptHtml required).

Sorry but it is currently useless - it segfaults.

%description egon -l pl
Egon Animator jest narzêdziem do tworzenia animacji bazowanym na
systemie X Window. Zasada dzia³ania polega na tym, ¿e "obiekty"
(prostok±ty, linie, obrazki itd.) s± dodawane do "sceny", gdzie
wykonuj± odpowiednie polecenia wskazuj±ce, kiedy i gdzie maj± siê
pojawiæ. Egon Animator jest czê¶ci± pakietu biurowego Siag Office.

Wspierane formaty plików: Egon Animator, ¼ród³o w jêzyku C, animowany
GIF, Postscript, tekst, HTML, Magic Point, MS Powerpoint (wymagany
program pptHtml).

Niestety chwilowo program jest bezu¿yteczny, gdy¿ wywo³uje naruszenie
ochrony pamiêci.

%package xedplus
Summary:	Siag Office simple but powerful text editor
Summary(pl):	Prosty lecz wydajny edytor tekstów Siag Office
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description xedplus
Simple text editor for editing config files or source code. It
contains everything you need including even commands to call sed.
Xedplus is a part of free Siag Office package.

%description xedplus -l pl
Prosty edytor tekstów do edycji plików konfiguracyjnych czy kodów
¼ród³owych. Posiada wszystko, czego potrzebujesz - nawet komendy, aby
wywo³aæ seda. Xedplus jest czê¶ci± pakietu biurowego Siag Office.

%package xfiler
Summary:	Siag Office file manager
Summary(pl):	Zarz±dca plików Siag Office
Group:		X11/Applications
Requires:	%{name} = %{version}

%description xfiler
Simple and easy to use file manager. It contains basic commands to
manage your filesystem. Suits almost all needs of plain user. Xfiler
is a part of free Siag Office package.

%description xfiler -l pl
Prosty i ³atwy w u¿yciu zarz±dca plików. Posiada podstawowe polecenia
zarz±dzania systemem plików. Spe³nia potrzeby zwyk³ego u¿ytkownika.
Xfiler jest czê¶ci± pakietu biurowego Siag Office.

%package plugins
Summary:	Plugins to use with Siag Office package
Summary(pl):	Wtyczki do u¿ywania z pakietem Siag Office
Group:		X11/Applications

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

%description plugins -l pl
Zawiera kilka wtyczek dla pakietu biurowego Siag Office (jest ich
trochê wiêcej ni¿ opisanych tutaj):

- The Image Plugin - wy¶wietla najbardziej popularne formaty plików
  je¶li jest zainstalowany zestaw konwerterów NETPBM. W przeciwnym
  wypadku bêdzie wy¶wietla³ tylko grafikê w formacie XPM.
- The Dummy Plugin - dzia³a jako swoisty interfejs pomiêdzy Siagiem a
  inna aplikacj±. Komunikuje siê protoko³em wtyczek ze Siag i robi, co
  potrafi, aby zarz±dzaæ zewnêtrzn± aplikacj±.
- The Hello Plugin - stworzony dla celów demonstracyjnych: wy¶wietla
  komunikat "Hello, World" w swoim oknie. Jest doskona³ym przyk³adem,
  który mo¿e pos³u¿yæ do stworzenia w pe³ni dzia³aj±cej wtyczki.

%package gvu
Summary:	Siag Office graphics previewer
Summary(pl):	Przegl±darka graficzna Siag Office
Group:		X11/Applications
Requires:	%{name} = %{version}

%description gvu
Gvu allows you to easily view Postscript (*.ps) and Encapsulated
Postsript (*.eps) files. It uses Aladdin Ghostscript software to
process files. Gvu is a part of free Siag Office package.

%description gvu -l pl
Gvu umo¿liwia ³atwe przegl±danie plików w formacie Postscript (*.ps)
oraz Encapsulated Postscript (*.eps). Wykorzystuje w tym celu
oprogramowanie Alladin Ghostscript. Gvu jest czê¶ci± pakietu biurowego
Siag Office.

%package -n XawM
Summary:	Modified version of X athena widgets in 3d (Xaw3d)
Summary(pl):	Zmodyfikowana wersja trójwymiarowych widgetów athena
Group:		X11/Libraries

%description -n XawM
XawM is modified version of X athena widgets in 3d (Xaw3d). It adds 3d
look to applications running under Xwindow.

%description -n XawM -l pl
XawM jest zmodyfikowan± wersj± trójowymiarowych widgetów atheny
(Xaw3d). Dodaje "trójwymiarowo¶æ" interfejsom aplikacji dzia³aj±cych
pod X Window.

%prep
%setup -q
#%patch -p1

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure2_13
%{__make} CFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/{Spreadsheets,Wordprocessors} \
	$RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers \
	$RPM_BUILD_ROOT{%{_applnkdir}/{Editors,Utilities},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/siag/examples/{pw,siag,egon}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Office/Spreadsheets
install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/Graphics
install %{SOURCE5} $RPM_BUILD_ROOT%{_applnkdir}/Office/Wordprocessors
install %{SOURCE6} $RPM_BUILD_ROOT%{_applnkdir}/Editors
install %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

install pw/examples/*.{doc,pw,html,rtf,txt,bmk} $RPM_BUILD_ROOT%{_datadir}/siag/examples/pw
install siag/examples/*.{wk1,siag,csv} $RPM_BUILD_ROOT%{_datadir}/siag/examples/siag
install egon/examples/*.egon $RPM_BUILD_ROOT%{_datadir}/siag/examples/egon

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n XawM -p /sbin/ldconfig
%postun -n XawM -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#FILES need patching
%doc AUTHORS ChangeLog FILES NEWS NLS README
%doc common/docs/Copyright
%doc common/docs/*.html
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
%{_mandir}/man1/siod.1*

%files siag
%defattr(644,root,root,755)
%doc siag/docs/README
%doc siag/docs/*.html
%doc siag/docs/*.gif
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
%{_datadir}/siag/examples/siag/*
%{_mandir}/man1/siag.1*
%{_applnkdir}/Office/Spreadsheets/siag.desktop
%{_pixmapsdir}/siag.png

%files pw
%defattr(644,root,root,755)
%doc pw/docs/*.html
%doc pw/docs/*.gif
%attr(755,root,root) %{_bindir}/pw
%{_datadir}/siag/pw/external.load
%{_datadir}/siag/pw/external.save
%{_datadir}/siag/pw/menu.scm
%{_datadir}/siag/pw/pw.scm
%{_datadir}/siag/pw/styles.scm
%{_datadir}/siag/common/bitmaps/pw.xpm
%{_datadir}/siag/common/bitmaps/ctab.xpm
%{_datadir}/siag/common/bitmaps/ltab.xpm
%{_datadir}/siag/common/bitmaps/rtab.xpm
%{_datadir}/siag/common/bitmaps/strike.xpm
%{_datadir}/siag/common/bitmaps/hfull.xpm
%{_datadir}/siag/examples/pw/*
%{_mandir}/man1/pw.1*
%{_applnkdir}/Office/Wordprocessors/pw.desktop
%{_pixmapsdir}/pw.png

%files egon
%defattr(644,root,root,755)
%doc egon/docs/*.html
%doc egon/docs/*.gif
%attr(755,root,root) %{_bindir}/egon
%{_datadir}/siag/egon/animator.scm
%{_datadir}/siag/egon/egon.scm
%{_datadir}/siag/egon/external.load
%{_datadir}/siag/egon/external.save
%{_datadir}/siag/egon/menu.scm
%{_datadir}/siag/common/bitmaps/egon.xpm
%{_datadir}/siag/examples/egon/*
%{_mandir}/man1/egon.1*
%{_applnkdir}/Graphics/egon.desktop
%{_pixmapsdir}/egon.png

%files xedplus
%defattr(644,root,root,755)
%doc xed/{README,xedplus.html}
%attr(755,root,root) %{_bindir}/xedplus
%{_datadir}/siag/common/bitmaps/xedplus.xpm
%{_mandir}/man1/xedplus.1*
%{_applnkdir}/Editors/xedplus.desktop
%{_pixmapsdir}/xedplus.png

%files xfiler
%defattr(644,root,root,755)
%doc xfiler/{README,xfiler.html}
%attr(755,root,root) %{_bindir}/xfiler
%attr(755,root,root) %{_bindir}/runcmd
%{_datadir}/siag/xfiler/FilesMagic
%{_datadir}/siag/xfiler/Filesrc
%attr(755,root,root) %{_datadir}/siag/xfiler/makeicons
%{_datadir}/siag/common/bitmaps/xfiler.xpm
%{_mandir}/man1/xfiler.1*
%{_applnkdir}/Utilities/xfiler.desktop
%{_pixmapsdir}/xfiler.png
#BITMAPS MISSING!!!

%files plugins
%defattr(644,root,root,755)
%doc plugins/README
%attr(755,root,root) %{_libdir}/siag/plugins/clipart
%attr(755,root,root) %{_libdir}/siag/plugins/dummy
%attr(755,root,root) %{_libdir}/siag/plugins/form
%attr(755,root,root) %{_libdir}/siag/plugins/hello
%attr(755,root,root) %{_libdir}/siag/plugins/image
%attr(755,root,root) %{_libdir}/siag/plugins/plot
%attr(755,root,root) %{_libdir}/siag/plugins/text
%{_datadir}/siag/plugins/dummy.scm
%{_datadir}/siag/plugins/plugin.scm
%{_mandir}/man1/dummy_plugin.1*

%files gvu
%defattr(644,root,root,755)
%doc gvu/README
%attr(755,root,root) %{_bindir}/gvu
%{_datadir}/siag/common/bitmaps/gvu.xpm
%{_mandir}/man1/gvu.1*
%{_applnkdir}/Graphics/Viewers/gvu.desktop
%{_pixmapsdir}/gvu.png

%files -n XawM
%defattr(644,root,root,755)
%doc XawM/README*
%attr(755,root,root) %{_libdir}/libXawM.so.*.*
