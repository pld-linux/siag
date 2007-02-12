Summary:	Siag Office
Summary(pl.UTF-8):	Pakiet biurowy Siag Office
Name:		siag
Version:	3.6.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://siag.nu/pub/siag/%{name}-%{version}.tar.gz
# Source0-md5:	bb7bb66dc9d3659fd11cdbac61ea6e13
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
BuildRequires:	Mowitz-devel
BuildRequires:	XFree86-devel
BuildRequires:	bzip2-devel
BuildRequires:	freetype1-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	ncurses-devel
BuildRequires:	neXtaw-devel
#BuildRequires:	python-devel
#BuildRequires:	tcl-devel
Obsoletes:	XawM
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Siag Office is a tightly integrated, fast and free office package. It
consists of the spreadsheet Siag, the word processor PW, the animation
program Egon, the text editor XedPlus, the file manager Xfiler and the
previewer Gvu.

Install this package if you want to use any of Siag Office programs.

%description -l pl.UTF-8
Siag Office jest ściśle zintegrowanym, szybkim darmowym pakietem
biurowym. Składa się z arkusza kalkulacyjnego Siag, procesora tekstów
PW, programu do animacji egon, edytora tekstowego XedPlus, zarządcy
plików Xfiler oraz przeglądarki Gvu.

%package siag
Summary:	Scheme In A Grid - Siag Office spreadsheet
Summary(pl.UTF-8):	Scheme In A Grid - arkusz kalkulacyjny Siag Office
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description siag
Siag is a spreadsheet based on X and Scheme. It has many, many
features. It contains even webserver! Siag is a part of free Siag
Office package.

Supported file formats: Siag, Comma Separated Values, Plain Text,
Lotus 1-2-3, Postscript, HTML Tables, Scheme Code, Troff Tables, LaTeX
Tables. Additional formats can be supported by using external
converters, such as xls2csv for Microsoft Excel.

%description siag -l pl.UTF-8
Siag jest arkuszem kalkulacyjnym bazującym na systemie X Window oraz
języku Scheme. Posiada wiele, bardzo wiele funkcji. Jest wyposażony
nawet w serwer WWW! Siag jest częścią pakietu biurowego Siag Office.

Wspierane formaty plików: Siag, wartości oddzielane przecinkami (Comma
Separated Values), tekst, Lotus 1-2-3, Postscript, tabelki HTML,
źródło Scheme, tabelki Troff oraz Latex. Dodatkowe formaty mogą być
obsłużone przy użyciu zewnętrznych konwerterów, np. xls2csv dla
Microsoft Excel.

%package pw
Summary:	Pathetic Writer - Siag Office word processor
Summary(pl.UTF-8):	Pathetic Writer - procesor tekstów Siag Office
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description pw
Pathetic Writer is an X-based word processor for Unix. It is a part of
free Siag Office package.

Supported file formats: Pathetic Writer, Plain Text, Postscript,
Hypertext Markup Language, Rich Text Format. Some of them require
using external converter called WV.

%description pw -l pl.UTF-8
Pathetic Writer jest procesorem tekstów bazowanym na systemie X
Window. Jest on częścią pakietu biurowego Siag Office.

Wspierane formaty plików: Pathetic Writer, tekst, Postscript, HTML,
RTF. Niektóre z nich wymagają zewnętrznego konwertera o nazwie WV.

%package egon
Summary:	Egon Animator - Siag Office animation software
Summary(pl.UTF-8):	Egon Animator - oprogramowanie do animacji Siag Office
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description egon
Egon Animator is an X-based animation development tool for Unix. The
idea is that "objects" (rectangles, lines, pixmaps and so on) are
added to a "stage" where they are then made to perform by telling them
where they should be and when. Egon Animator is a part of free Siag
Office package.

Supported file formats: Egon Animator, C source, Animated GIF,
Postscript, Text, HTML, Magic Point, MS Powerpoint (pptHtml required).

Sorry but it is currently useless - it segfaults.

%description egon -l pl.UTF-8
Egon Animator jest narzędziem do tworzenia animacji bazowanym na
systemie X Window. Zasada działania polega na tym, że "obiekty"
(prostokąty, linie, obrazki itd.) są dodawane do "sceny", gdzie
wykonują odpowiednie polecenia wskazujące, kiedy i gdzie mają się
pojawić. Egon Animator jest częścią pakietu biurowego Siag Office.

Wspierane formaty plików: Egon Animator, źródło w języku C, animowany
GIF, Postscript, tekst, HTML, Magic Point, MS Powerpoint (wymagany
program pptHtml).

Niestety chwilowo program jest bezużyteczny, gdyż wywołuje naruszenie
ochrony pamięci.

%package xedplus
Summary:	Siag Office simple but powerful text editor
Summary(pl.UTF-8):	Prosty lecz wydajny edytor tekstów Siag Office
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}-%{release}

%description xedplus
Simple text editor for editing config files or source code. It
contains everything you need including even commands to call sed.
Xedplus is a part of free Siag Office package.

%description xedplus -l pl.UTF-8
Prosty edytor tekstów do edycji plików konfiguracyjnych czy kodów
źródłowych. Posiada wszystko, czego potrzebujesz - nawet komendy, aby
wywołać seda. Xedplus jest częścią pakietu biurowego Siag Office.

%package xfiler
Summary:	Siag Office file manager
Summary(pl.UTF-8):	Zarządca plików Siag Office
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description xfiler
Simple and easy to use file manager. It contains basic commands to
manage your filesystem. Suits almost all needs of plain user. Xfiler
is a part of free Siag Office package.

%description xfiler -l pl.UTF-8
Prosty i łatwy w użyciu zarządca plików. Posiada podstawowe polecenia
zarządzania systemem plików. Spełnia potrzeby zwykłego użytkownika.
Xfiler jest częścią pakietu biurowego Siag Office.

%package plugins
Summary:	Plugins to use with Siag Office package
Summary(pl.UTF-8):	Wtyczki do używania z pakietem Siag Office
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

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

%description plugins -l pl.UTF-8
Zawiera kilka wtyczek dla pakietu biurowego Siag Office (jest ich
trochę więcej niż opisanych tutaj):

- The Image Plugin - wyświetla najbardziej popularne formaty plików
  jeśli jest zainstalowany zestaw konwerterów NETPBM. W przeciwnym
  wypadku będzie wyświetlał tylko grafikę w formacie XPM.
- The Dummy Plugin - działa jako swoisty interfejs pomiędzy Siagiem a
  inna aplikacją. Komunikuje się protokołem wtyczek ze Siag i robi, co
  potrafi, aby zarządzać zewnętrzną aplikacją.
- The Hello Plugin - stworzony dla celów demonstracyjnych: wyświetla
  komunikat "Hello, World" w swoim oknie. Jest doskonałym przykładem,
  który może posłużyć do stworzenia w pełni działającej wtyczki.

%package gvu
Summary:	Siag Office graphics previewer
Summary(pl.UTF-8):	Przeglądarka graficzna Siag Office
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gvu
Gvu allows you to easily view Postscript (*.ps) and Encapsulated
Postsript (*.eps) files. It uses Aladdin Ghostscript software to
process files. Gvu is a part of free Siag Office package.

%description gvu -l pl.UTF-8
Gvu umożliwia łatwe przeglądanie plików w formacie Postscript (*.ps)
oraz Encapsulated Postscript (*.eps). Wykorzystuje w tym celu
oprogramowanie Alladin Ghostscript. Gvu jest częścią pakietu biurowego
Siag Office.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure2_13
%{__make} \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_datadir}/siag/examples/{pw,siag,egon}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
	$RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

install pw/examples/*.{doc,pw,html,rtf,txt,bmk} $RPM_BUILD_ROOT%{_datadir}/siag/examples/pw
install siag/examples/*.{wk1,siag,csv} $RPM_BUILD_ROOT%{_datadir}/siag/examples/siag
install egon/examples/*.egon $RPM_BUILD_ROOT%{_datadir}/siag/examples/egon

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#FILES need patching
%doc AUTHORS ChangeLog FILES NEWS NLS README
%doc common/docs/Copyright
%doc common/docs/*.html
%attr(755,root,root) %{_bindir}/mgptotxt
%attr(755,root,root) %{_bindir}/siaghelp
%attr(755,root,root) %{_bindir}/siagrun
%dir %{_datadir}/siag
%dir %{_datadir}/siag/common
%attr(755,root,root) %{_datadir}/siag/common/any2xpm
%{_datadir}/siag/common/common.scm
#here should be something with lang or not?
%{_datadir}/siag/common/dictionary.*
%{_datadir}/siag/common/position.scm
%{_datadir}/siag/common/tools.scm
%dir %{_datadir}/siag/common/bitmaps
%{_datadir}/siag/common/bitmaps/addressbook.xpm
%{_datadir}/siag/common/bitmaps/SO3.xpm
%{_datadir}/siag/common/bitmaps/back.xpm
%{_datadir}/siag/common/bitmaps/blank.xpm
%{_datadir}/siag/common/bitmaps/bold.xpm
%{_datadir}/siag/common/bitmaps/book-closed.xpm
%{_datadir}/siag/common/bitmaps/book-open.xpm
%{_datadir}/siag/common/bitmaps/borders.xpm
%{_datadir}/siag/common/bitmaps/cancel.xpm
%{_datadir}/siag/common/bitmaps/center.xpm
%{_datadir}/siag/common/bitmaps/composer.xpm
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
%{_datadir}/siag/common/bitmaps/mail.xpm
%{_datadir}/siag/common/bitmaps/navigator.xpm
%{_datadir}/siag/common/bitmaps/netscape.xpm
%{_datadir}/siag/common/bitmaps/new.xpm
%{_datadir}/siag/common/bitmaps/news.xpm
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
%{_datadir}/siag/common/bitmaps/security.xpm
%{_datadir}/siag/common/bitmaps/siagoffice.xpm
%{_datadir}/siag/common/bitmaps/sigma.xpm
%{_datadir}/siag/common/bitmaps/smaller.xpm
%{_datadir}/siag/common/bitmaps/sortaz.xpm
%{_datadir}/siag/common/bitmaps/sortmode.xpm
%{_datadir}/siag/common/bitmaps/sortza.xpm
%{_datadir}/siag/common/bitmaps/spell.xpm
%{_datadir}/siag/common/bitmaps/stop.xpm
%{_datadir}/siag/common/bitmaps/table.xpm
%{_datadir}/siag/common/bitmaps/uchar.xpm
%{_datadir}/siag/common/bitmaps/uline.xpm
%{_datadir}/siag/common/bitmaps/undo.xpm
%{_datadir}/siag/common/bitmaps/unknown.xpm
%{_datadir}/siag/common/bitmaps/vbottom.xpm
%{_datadir}/siag/common/bitmaps/viewmode.xpm
%{_datadir}/siag/common/bitmaps/vtop.xpm
%{_datadir}/siag/common/bitmaps/xterm16.xpm
%{_datadir}/siag/common/bitmaps/kde
%{_datadir}/siag/common/bitmaps/kde2
%{_datadir}/siag/common/bitmaps/ms
%{_datadir}/siag/common/bitmaps/gnome
%dir %{_datadir}/siag/common/themes
%{_datadir}/siag/common/themes/theme.athena
%{_datadir}/siag/common/themes/theme.classic
%{_datadir}/siag/common/themes/theme.gnome
%{_datadir}/siag/common/themes/theme.kde
%{_datadir}/siag/common/themes/theme.kde2
%{_datadir}/siag/common/themes/theme.ms
%dir %{_datadir}/siag/examples
%dir %{_datadir}/siag/siod
%{_datadir}/siag/siod/siod.scm
%dir %{_datadir}/siag/xcommon
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
%dir %{_datadir}/siag/siag
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
%{_datadir}/siag/siag/ccmath.scm
%{_datadir}/siag/siag/functions.scm
%{_datadir}/siag/siag/trans.scm
%{_datadir}/siag/common/bitmaps/siag.xpm
%{_datadir}/siag/examples/siag
%{_mandir}/man1/siag.1*
%{_desktopdir}/siag.desktop
%{_pixmapsdir}/siag.png

%files pw
%defattr(644,root,root,755)
%doc pw/docs/*.html
%doc pw/docs/*.gif
%attr(755,root,root) %{_bindir}/pw
%dir %{_datadir}/siag/pw
%{_datadir}/siag/pw/external.load
%{_datadir}/siag/pw/external.save
%{_datadir}/siag/pw/menu.scm
%{_datadir}/siag/pw/pw.scm
%{_datadir}/siag/pw/styles.scm
%{_datadir}/siag/common/bitmaps/pw.xpm
%{_datadir}/siag/common/bitmaps/strike.xpm
%{_datadir}/siag/common/bitmaps/hfull.xpm
%{_datadir}/siag/examples/pw
%{_mandir}/man1/pw.1*
%{_desktopdir}/pw.desktop
%{_pixmapsdir}/pw.png

%files egon
%defattr(644,root,root,755)
%doc egon/docs/*.html
%doc egon/docs/*.gif
%attr(755,root,root) %{_bindir}/egon
%dir %{_datadir}/siag/egon
%{_datadir}/siag/egon/animator.scm
%{_datadir}/siag/egon/egon.scm
%{_datadir}/siag/egon/external.load
%{_datadir}/siag/egon/external.save
%{_datadir}/siag/egon/menu.scm
%{_datadir}/siag/common/bitmaps/egon.xpm
%{_datadir}/siag/examples/egon
%{_mandir}/man1/egon.1*
%{_desktopdir}/egon.desktop
%{_pixmapsdir}/egon.png

%files xedplus
%defattr(644,root,root,755)
%doc xed/{README,xedplus.html}
%attr(755,root,root) %{_bindir}/xedplus
%{_datadir}/siag/common/bitmaps/xedplus.xpm
%{_mandir}/man1/xedplus.1*
%{_desktopdir}/xedplus.desktop
%{_pixmapsdir}/xedplus.png

%files xfiler
%defattr(644,root,root,755)
%doc xfiler/{README,xfiler.html}
%attr(755,root,root) %{_bindir}/xfiler
%attr(755,root,root) %{_bindir}/runcmd
%dir %{_datadir}/siag/xfiler
%{_datadir}/siag/xfiler/FilesMagic
%{_datadir}/siag/xfiler/Filesrc
%attr(755,root,root) %{_datadir}/siag/xfiler/makeicons
%{_datadir}/siag/common/bitmaps/xfiler.xpm
%{_mandir}/man1/xfiler.1*
%{_mandir}/man1/runcmd.1*
%{_desktopdir}/xfiler.desktop
%{_pixmapsdir}/xfiler.png
#BITMAPS MISSING!!!

%files plugins
%defattr(644,root,root,755)
%doc plugins/README
%dir %{_libdir}/siag
%dir %{_libdir}/siag/plugins
%attr(755,root,root) %{_libdir}/siag/plugins/clipart
%attr(755,root,root) %{_libdir}/siag/plugins/dummy
%attr(755,root,root) %{_libdir}/siag/plugins/form
%attr(755,root,root) %{_libdir}/siag/plugins/hello
%attr(755,root,root) %{_libdir}/siag/plugins/image
%attr(755,root,root) %{_libdir}/siag/plugins/plot
%attr(755,root,root) %{_libdir}/siag/plugins/text
%dir %{_datadir}/siag/plugins
%{_datadir}/siag/plugins/dummy.scm
%{_datadir}/siag/plugins/plugin.scm
%{_mandir}/man1/dummy_plugin.1*

%files gvu
%defattr(644,root,root,755)
%doc gvu/README
%attr(755,root,root) %{_bindir}/gvu
%{_datadir}/siag/common/bitmaps/gvu.xpm
%{_mandir}/man1/gvu.1*
%{_desktopdir}/gvu.desktop
%{_pixmapsdir}/gvu.png
