Summary:	Siag Office
Name:		siag
Version:	3.3.10
Release: 3
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	ftp://siag.nu/pub/siag/%{name}-%{version}.tar.gz
URL:		http://siag.nu/
#When builded with script languages enable those
#BuildRequires:	tcl-devel
#BuildRequires: python-devel
#BuildRequires: XawM-devel - missing in PLD so built from siag
#BuildRequires: xpm-devel
BuildRequires:	XFree86-devel
BuildRequires:	bzip2-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr
#%define		_mandir		%{_prefix}/man

%description
Siag Office is a free office package for Unix, including word
processor, spreadsheet and presentation graphics. It is a bundling of
the spreadsheet SIAG, the word processor WP and the Animation program
Egon.

%prep
%setup -q 

%build
#is it really needed?
autoconf
CFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/ncurses" ./configure --prefix=/usr
%{__make} 
#it is necessary if you are building siag and have installed older version
cd XawM
CFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/ncurses" ./configure --prefix=/usr
cd ..

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT/usr 
install common/{rgb,fonts}.txt $RPM_BUILD_ROOT/usr/share/siag/common
install common/bitmaps/{handlebg,save,lline,rline}.xpm $RPM_BUILD_ROOT/usr/share/siag/common/bitmaps
cd XawM
%{__make} install prefix=$RPM_BUILD_ROOT/usr

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog  FILES INSTALL NEWS NLS README
%doc common/docs/Copyright
%doc common/docs/credits.html
%doc common/docs/embedding.html
%doc common/docs/form.html
%doc common/docs/interpreters.html
%doc common/docs/office.html
%doc common/docs/plugins.html
%doc common/docs/search.html
%doc common/docs/siaghelp.html
%doc common/docs/siaghelp
%doc egon/docs/COPYING
%doc egon/docs/TODO
%doc egon/docs/BUGS
#%doc egon/docs/CHANGES
%doc egon/docs/commands.html
%doc egon/docs/concepts.html
%doc egon/docs/egon.gif
%doc egon/docs/egon.html
%doc egon/docs/fileformats.html
%doc egon/docs/intro.html
%doc egon/docs/invocation.html
%doc egon/docs/keys.html
%doc egon/docs/mouse.html
%doc egon/docs/scheme.html
%doc egon/docs/scrollbars.html
%doc egon/docs/strings.html
%doc egon/docs/toolbar.html
%doc pw/docs/COPYING
%doc pw/docs/TODO
%doc pw/docs/BUGS
#%doc pw/docs/CHANGES
%doc pw/docs/commands.html
%doc pw/docs/concepts.html
%doc pw/docs/fileformats.html
%doc pw/docs/intro.html
%doc pw/docs/invocation.html
%doc pw/docs/keys.html
%doc pw/docs/mouse.html
%doc pw/docs/pw.gif
%doc pw/docs/pw.html
%doc pw/docs/scheme.html
%doc pw/docs/scrollbars.html
%doc pw/docs/spell.html
%doc pw/docs/strings.html
%doc pw/docs/toolbar.html
%doc siag/docs/README
%doc siag/docs/COPYING
%doc siag/docs/TODO
%doc siag/docs/BUGS
#%doc siag/docs/CHANGES
%doc siag/docs/c-expr.html
%doc siag/docs/commands.html
%doc siag/docs/concepts.html
%doc siag/docs/fileformats.html
%doc siag/docs/form.html
%doc siag/docs/gnuplot.html
#%doc siag/docs/howto.html
%doc siag/docs/intro.html
%doc siag/docs/invocation.html
%doc siag/docs/keys.html
%doc siag/docs/mouse.html
%doc siag/docs/scheme.html
%doc siag/docs/scrollbars.html
%doc siag/docs/siag.gif
%doc siag/docs/siag.html
%doc siag/docs/strings.html
%doc siag/docs/toolbar.html
%doc siod/docs/siod.html
%doc xcommon/docs/TODO
#%doc xcommon/docs/CHANGES
%doc xcommon/docs/filesel.html
#fix it later
#/usr/man/man1/siod.1
#/usr/man/man1/siag.1
#/usr/man/man1/pw.1
#/usr/man/man1/egon.1
#/usr/man/man1/dummy_plugin.1
%{_datadir}/siag/siod/siod.scm
%{_datadir}/siag/common/bitmaps/blank.xpm
%{_datadir}/siag/common/bitmaps/bold.xpm
%{_datadir}/siag/common/bitmaps/borders.xpm
%{_datadir}/siag/common/bitmaps/copy.xpm
%{_datadir}/siag/common/bitmaps/copyright.xpm
%{_datadir}/siag/common/bitmaps/cut.xpm
#%{_datadir}/siag/common/bitmaps/egon_fg.xpm
%{_datadir}/siag/common/bitmaps/fld_open.xpm
#%{_datadir}/siag/common/bitmaps/floppy3.xpm
%{_datadir}/siag/common/bitmaps/grid.xpm
%{_datadir}/siag/common/bitmaps/hcenter.xpm
%{_datadir}/siag/common/bitmaps/hleft.xpm
%{_datadir}/siag/common/bitmaps/hright.xpm
%{_datadir}/siag/common/bitmaps/info.xpm
%{_datadir}/siag/common/bitmaps/italic.xpm
%{_datadir}/siag/common/bitmaps/new.xpm
%{_datadir}/siag/common/bitmaps/next.xpm
%{_datadir}/siag/common/bitmaps/none.xpm
%{_datadir}/siag/common/bitmaps/paste.xpm
%{_datadir}/siag/common/bitmaps/play.xpm
%{_datadir}/siag/common/bitmaps/plotter.xpm
%{_datadir}/siag/common/bitmaps/preview.xpm
%{_datadir}/siag/common/bitmaps/previous.xpm
%{_datadir}/siag/common/bitmaps/printer.xpm
#%{_datadir}/siag/common/bitmaps/pw_fg.xpm
%{_datadir}/siag/common/bitmaps/redo.xpm
#%{_datadir}/siag/common/bitmaps/siag_fg.xpm
%{_datadir}/siag/common/bitmaps/sigma.xpm
%{_datadir}/siag/common/bitmaps/sortaz.xpm
%{_datadir}/siag/common/bitmaps/sortza.xpm
%{_datadir}/siag/common/bitmaps/spell.xpm
%{_datadir}/siag/common/bitmaps/stop.xpm
%{_datadir}/siag/common/bitmaps/uchar.xpm
%{_datadir}/siag/common/bitmaps/uline.xpm
%{_datadir}/siag/common/bitmaps/undo.xpm
%{_datadir}/siag/common/bitmaps/vbottom.xpm
%{_datadir}/siag/common/bitmaps/vtop.xpm
%{_datadir}/siag/common/bitmaps/back.xpm
%{_datadir}/siag/common/bitmaps/cancel.xpm
%{_datadir}/siag/common/bitmaps/home.xpm
%{_datadir}/siag/common/bitmaps/quit.xpm
%{_datadir}/siag/common/bitmaps/reload.xpm
%{_datadir}/siag/common/bitmaps/search.xpm
%{_datadir}/siag/common/bitmaps/handlebg.xpm
%{_datadir}/siag/common/bitmaps/save.xpm
%{_datadir}/siag/common/bitmaps/lline.xpm
%{_datadir}/siag/common/bitmaps/rline.xpm
#%{_datadir}/siag/common/bitmaps/ksiag.xpm
%{_datadir}/siag/common/any2xpm
#%{_datadir}/siag/common/colors.scm
#%{_datadir}/siag/common/fonts.scm
%{_datadir}/siag/common/tools.scm
%{_datadir}/siag/common/common.scm
%{_datadir}/siag/common/dictionary.sv
%{_datadir}/siag/common/dictionary.es
%{_datadir}/siag/common/dictionary.de
%{_datadir}/siag/common/dictionary.fr
%{_datadir}/siag/common/dictionary.no
%{_datadir}/siag/common/rgb.txt
%{_datadir}/siag/common/fonts.txt
%{_datadir}/siag/xcommon/StringDefs.scm
%{_datadir}/siag/xcommon/form.scm
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
%{_datadir}/siag/siag/usermgr.scm
%{_datadir}/siag/pw/external.load
%{_datadir}/siag/pw/external.save
%{_datadir}/siag/pw/menu.scm
%{_datadir}/siag/pw/pw.scm
%{_datadir}/siag/pw/styles.scm
%{_datadir}/siag/egon/animator.scm
%{_datadir}/siag/egon/egon.scm
%{_datadir}/siag/egon/menu.scm
%{_datadir}/siag/egon/external.load
%{_datadir}/siag/egon/external.save
%{_datadir}/siag/plugins/dummy.scm
%{_datadir}/siag/plugins/plugin.scm
%attr(755,root,root) %{_bindir}/siag
%attr(755,root,root) %{_bindir}/pw
%attr(755,root,root) %{_bindir}/egon
#move it later somwhere ;>
#%{_libdir}exec/siag/plugins/dummy
#%{_libdir}exec/siag/plugins/image
#%{_libdir}exec/siag/plugins/hello
/usr/lib/libXawM.so
/usr/lib/libXawM.so.0
/usr/lib/libXawM.so.0.0.0
