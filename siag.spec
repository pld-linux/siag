Summary:	Siag Office
Name:		siag
Version:	3.3.11
Release:	0
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	ftp://siag.nu/pub/siag/%{name}-%{version}.tar.bz2
URL:		http://siag.nu/
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

%define		_prefix		/usr

%description
Siag Office is a tightly integrated, free office package. It consists of
the spreadsheet Siag, the word processor PW, the animation program Egon,
the text editor XedPlus, the file manager Xfiler and the previewer Gvu.

Install this package if you want to use any of Siag Office programs. 

%package siag
Summary: Scheme In A Grid - spreadsheet for Siag Office
Group: X11/Applications

%description siag
Siag is a spreadsheet based on X and Scheme. It has many, many features.
It contains even webserver! It is a part of free Siag Office package.

Supported file formats: Siag, Comma Separated Values, Plain Text,
Lotus 1-2-3, Postscript, HTML Tables, Scheme Code, Troff Tables, LaTeX Tables.
Additional formats can be supported by using external converters, such as
xls2cvs for Microsoft Excel.

%package pw
Summary: Pathetic Writer - word processor for Siag Office
Group: X11/Applications

%description pw
Pathetic Writer is an X-based word processor for Unix. It is a part of free
Siag Office package.

Supported file formats: Pathetic Writer, Plain Text, Postscript, Hypertext
Markup Language, Rich Text Format. Some of them require using external
converter called WV.

%package egon
Summary: Egon Animator - animation software for Siag Office
Group: X11/Applications

%description egon
Egon Animator is an X-based animation development tool for Unix. The idea
is that "objects" (rectangles, lines, pixmaps and so on) are added to a "stage"
where they are then made to perform by telling them where they should be
and when. It is a part of free Siag Office package.

Supported file formats: Egon Animator, C source, Animated GIF, Postscript,
Text, HTML, Magic Point, MS Powerpoint (pptHtml required).

%package xedplus
Summary: Simple but powerful text editor for Siag Office package
Group: X11/Applications

%description xedplus


%package xfiler
Summary: File manager for Siag Office package
Group: X11/Applications

%description xfiler
Simple and easy to use file manager. It contains basic commands to manage
your filesystem. Suits almost all needs of plain user. It is a part of free
Siag Office package.

%package plugins
Summary: Plugins to use with Siag Office package
Group: X11/Applications

%description plugins
It contains some plugins for Siag Office package (there are some more not
mentioned here):

* The Image Plugin
It displays most common image formats if the NETPBM collection of  graphics  converters  is  installed.  Otherwise it will be able to display XPM images.
* The Dummy Plugin
The dummy application works as a "shim" between Siag and another application.
It speaks the plugin protocol with Siag and does its best to manage the
external application.
* The Hello Plugin
This one is for demonstrational purposes only: it displays the message
"Hello, World" in its window. It is suitable as an example of a simple plugin,
in that it contains all the necessary code to make a plugin of a normal
X program.

%package gvu
Summary: Graphics previewer for Siag Office package
Group: X11/Applications

%description gvu

%package -n XawM
Summary: Modified version of X athena widgets in 3d (Xaw3d)
Group: X11/Applications

%description -n XawM

%prep
%setup -q 

%build
%configure --without-stocks
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf {common,siag,pw,egon,siod}/docs/* xed/{README,TODO,xedplus.html} \
          xfiler/{README,TODO,xfiler.html} plugins/{README,TODO} \
	  XawM/README{,.Linux,.XAW3D,.XawM} $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%post -n XawM -p /sbin/ldconfig
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
#FILES need patching, GZIP HERE!!!
%doc AUTHORS ChangeLog FILES NEWS NLS README
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
%{_mandir}/man1/siod.1.gz

%files siag
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
%{_mandir}/man1/siag.1.gz

%files pw
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
%{_mandir}/man1/pw.1.gz

%files egon
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
%{_mandir}/man1/egon.1.gz

%files xedplus
%attr(755,root,root) %{_bindir}/xedplus
%doc xed/README.gz
%doc xed/TODO.gz
%doc xed/xedplus.html.gz
%{_mandir}/man1/xedplus.1.gz

%files xfiler
%attr(755,root,root) %{_bindir}/xfiler
%attr(755,root,root) %{_bindir}/runcmd
%{_datadir}/siag/xfiler/FilesMagic
%{_datadir}/siag/xfiler/Filesrc
%attr(755,root,root) %{_datadir}/siag/xfiler/makeicons
%doc xfiler/README.gz
%doc xfiler/TODO.gz
%doc xfiler/xfiler.html.gz
%{_mandir}/man1/xfiler.1.gz
#BITMAPS MISSING!!!

%files plugins
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
%{_mandir}/man1/dummy_plugin.1.gz

%files gvu
%attr(755,root,root) %{_bindir}/gvu
%doc gvu/README.gz
%doc gvu/TODO.gz
%{_mandir}/man1/gvu.1.gz

%files -n XawM
%{_libdir}/libXawM.so.0.0.0
%doc XawM/README.gz
%doc XawM/README.Linux.gz
%doc XawM/README.XAW3D.gz
%doc XawM/README.XawM.gz
