Summary:	Siag Office
Name:		siag
Version:	3.1.6
Release:	1
Copyright:	GPL
Group:		X11/Applications
Source:		ftp://ftp.edu.stockholm.se/pub/siag/%{name}-%{version}.tar.gz
URL:		http://www.edu.stockholm.se/siag/
#Requires: guile tcl Xaw3d
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Siag Office is a free office package for Unix, including word processor,
spreadsheet and presentation graphics. It is a bundling of the spreadsheet
SIAG, the word processor WP and the Animation program Egon. 

%prep
%setup 

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
make install prefix=$RPM_BUILD_ROOT/usr 

%files
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
%doc egon/docs/CHANGES
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
%doc pw/docs/CHANGES
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
%doc siag/docs/CHANGES
%doc siag/docs/c-expr.html
%doc siag/docs/commands.html
%doc siag/docs/concepts.html
%doc siag/docs/fileformats.html
%doc siag/docs/form.html
%doc siag/docs/gnuplot.html
%doc siag/docs/howto.html
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
%doc xcommon/docs/CHANGES
%doc xcommon/docs/filesel.html
/usr/man/man1/siod.1
/usr/man/man1/siag.1
/usr/man/man1/pw.1
/usr/man/man1/egon.1
/usr/man/man1/dummy_plugin.1
/usr/share/siag/siod/siod.scm
/usr/share/siag/common/bitmaps/blank.xpm
/usr/share/siag/common/bitmaps/bold.xpm
/usr/share/siag/common/bitmaps/borders.xpm
/usr/share/siag/common/bitmaps/copy.xpm
/usr/share/siag/common/bitmaps/copyright.xpm
/usr/share/siag/common/bitmaps/cut.xpm
/usr/share/siag/common/bitmaps/egon_fg.xpm
/usr/share/siag/common/bitmaps/fld_open.xpm
/usr/share/siag/common/bitmaps/floppy3.xpm
/usr/share/siag/common/bitmaps/grid.xpm
/usr/share/siag/common/bitmaps/hcenter.xpm
/usr/share/siag/common/bitmaps/hleft.xpm
/usr/share/siag/common/bitmaps/hright.xpm
/usr/share/siag/common/bitmaps/info.xpm
/usr/share/siag/common/bitmaps/italic.xpm
/usr/share/siag/common/bitmaps/new.xpm
/usr/share/siag/common/bitmaps/next.xpm
/usr/share/siag/common/bitmaps/none.xpm
/usr/share/siag/common/bitmaps/paste.xpm
/usr/share/siag/common/bitmaps/play.xpm
/usr/share/siag/common/bitmaps/plotter.xpm
/usr/share/siag/common/bitmaps/preview.xpm
/usr/share/siag/common/bitmaps/previous.xpm
/usr/share/siag/common/bitmaps/printer.xpm
/usr/share/siag/common/bitmaps/pw_fg.xpm
/usr/share/siag/common/bitmaps/redo.xpm
/usr/share/siag/common/bitmaps/siag_fg.xpm
/usr/share/siag/common/bitmaps/sigma.xpm
/usr/share/siag/common/bitmaps/sortaz.xpm
/usr/share/siag/common/bitmaps/sortza.xpm
/usr/share/siag/common/bitmaps/spell.xpm
/usr/share/siag/common/bitmaps/stop.xpm
/usr/share/siag/common/bitmaps/uchar.xpm
/usr/share/siag/common/bitmaps/uline.xpm
/usr/share/siag/common/bitmaps/undo.xpm
/usr/share/siag/common/bitmaps/vbottom.xpm
/usr/share/siag/common/bitmaps/vtop.xpm
/usr/share/siag/common/bitmaps/back.xpm
/usr/share/siag/common/bitmaps/cancel.xpm
/usr/share/siag/common/bitmaps/home.xpm
/usr/share/siag/common/bitmaps/quit.xpm
/usr/share/siag/common/bitmaps/reload.xpm
/usr/share/siag/common/bitmaps/search.xpm
/usr/share/siag/common/bitmaps/ksiag.xpm
/usr/share/siag/common/any2xpm
/usr/share/siag/common/colors.scm
/usr/share/siag/common/fonts.scm
/usr/share/siag/common/tools.scm
/usr/share/siag/common/dictionary.sv
/usr/share/siag/common/dictionary.es
/usr/share/siag/common/dictionary.de
/usr/share/siag/common/dictionary.fr
/usr/share/siag/common/dictionary.no
/usr/share/siag/xcommon/StringDefs.scm
/usr/share/siag/xcommon/form.scm
/usr/share/siag/siag/123.scm
/usr/share/siag/siag/data.scm
/usr/share/siag/siag/external.load
/usr/share/siag/siag/external.save
/usr/share/siag/siag/filemgr.scm
/usr/share/siag/siag/find.scm
/usr/share/siag/siag/keytable.scm
/usr/share/siag/siag/mailto.scm
/usr/share/siag/siag/menu.scm
/usr/share/siag/siag/plot.scm
/usr/share/siag/siag/siag-http.scm
/usr/share/siag/siag/siag-net.scm
/usr/share/siag/siag/siag.scm
/usr/share/siag/siag/sort.scm
/usr/share/siag/siag/splot.scm
/usr/share/siag/siag/styles.scm
/usr/share/siag/siag/usermgr.scm
/usr/share/siag/pw/external.load
/usr/share/siag/pw/external.save
/usr/share/siag/pw/menu.scm
/usr/share/siag/pw/pw.scm
/usr/share/siag/pw/styles.scm
/usr/share/siag/egon/animator.scm
/usr/share/siag/egon/egon.scm
/usr/share/siag/egon/menu.scm
/usr/share/siag/egon/external.load
/usr/share/siag/egon/external.save
/usr/share/siag/plugins/dummy.scm
/usr/share/siag/plugins/plugin.scm
/usr/bin/siag
/usr/bin/pw
/usr/bin/egon
/usr/libexec/siag/plugins/dummy
/usr/libexec/siag/plugins/image
/usr/libexec/siag/plugins/hello

%changelog
* Sat Feb 20 1999 Pablo Costa <pablo@shark.ib.usp.br>
- upgrade to the version 3.1.6
- Compile with quile, tcl and Xaw3d

* Sat Jan  2 1999 Kjetil Wiekhorst Jørgensen <jorgens+rpm@pvv.org>

- upgraded to version 3.1.3

* Wed Dec  2 1998 Kjetil Wiekhorst Jørgensen <jorgens+rpm@pvv.org>
- upgraded to version 3.1.0

* Sat Jul 4 1998 Jason Spangler <jasons@usemail.com>
  - initial creation of RPM
