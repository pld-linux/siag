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
#BuildRequires:	xpm-devel
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
Siag Office is a free office package for Unix, including word
processor, spreadsheet and presentation graphics. It is a bundling of
the spreadsheet SIAG, the word processor WP and the Animation program
Egon.

%prep
%setup -q 

%build
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses" ./configure --prefix=%{_prefix}
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install prefix=$RPM_BUILD_ROOT/%{_prefix} 

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

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
%{_datadir}/siag/xcommon/StringDefs.scm
%{_datadir}/siag/xcommon/form.scm
#FILES need patching
%doc AUTHORS ChangeLog FILES NEWS NLS README
%doc common/docs/Copyright
%doc common/docs/credits.html
%doc common/docs/embedding.html
%doc common/docs/form.html
%doc common/docs/interpreters.html
%doc common/docs/office.html
%doc common/docs/plugins.html
%doc common/docs/search.html
%doc common/docs/siaghelp.html
%doc xcommon/docs/TODO

#%files siag
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
%doc siag/docs/*
%doc siag/docs/BUGS
%doc siag/docs/README
%doc siag/docs/TODO
%doc siag/docs/c-expr.html
%doc siag/docs/commands.html
%doc siag/docs/concepts.html
%doc siag/docs/fileformats.html
%doc siag/docs/form.html
%doc siag/docs/gnuplot.html
%doc siag/docs/intro.html
%doc siag/docs/invocation.html
%doc siag/docs/keys.html
%doc siag/docs/mouse.html
%doc siag/docs/scheme.html
%doc siag/docs/scrollbars.html
%doc siag/docs/siag.gif
%doc siag/docs/siag.html
%doc siag/docs/strings.html
#%doc siag/examples/*
%{_prefix}/man/man1/siag.1

#%files pw
%attr(755,root,root) %{_bindir}/pw
%{_datadir}/siag/pw/external.load
%{_datadir}/siag/pw/external.save
%{_datadir}/siag/pw/menu.scm
%{_datadir}/siag/pw/pw.scm
%{_datadir}/siag/pw/styles.scm
%doc pw/docs/BUGS
%doc pw/docs/TODO
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
#%doc pw/examples/*
%{_prefix}/man/man1/pw.1

#%files egon
%attr(755,root,root) %{_bindir}/egon
%{_datadir}/siag/egon/animator.scm
%{_datadir}/siag/egon/egon.scm
%{_datadir}/siag/egon/external.load
%{_datadir}/siag/egon/external.save
%{_datadir}/siag/egon/menu.scm
%doc egon/docs/BUGS
%doc egon/docs/TODO
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
#%doc egon/examples/*
%{_prefix}/man/man1/egon.1

#%files xedplus maybe core?
%attr(755,root,root) %{_bindir}/xedplus
%doc xed/README
%doc xed/TODO
%doc xed/xedplus.html
%{_prefix}/man/man1/xedplus.1

#%files xfiler
%attr(755,root,root) %{_bindir}/xfiler
%attr(755,root,root) %{_bindir}/runcmd
%{_datadir}/siag/xfiler/FilesMagic
%{_datadir}/siag/xfiler/Filesrc
%attr(755,root,root) %{_datadir}/siag/xfiler/makeicons
%doc xfiler/README
%doc xfiler/TODO
%doc xfiler/xfiler.html
%{_prefix}/man/man1/xfiler.1
#BITMAPS MISSING!!!

#%files plugins
%attr(755,root,root) %{_libdir}exec/siag/plugins/clipart
%attr(755,root,root) %{_libdir}exec/siag/plugins/dummy
%attr(755,root,root) %{_libdir}exec/siag/plugins/form
%attr(755,root,root) %{_libdir}exec/siag/plugins/hello
%attr(755,root,root) %{_libdir}exec/siag/plugins/image
%attr(755,root,root) %{_libdir}exec/siag/plugins/plot
%attr(755,root,root) %{_libdir}exec/siag/plugins/text
%doc plugins/README
%doc plugins/TODO
%{_datadir}/siag/plugins/dummy.scm
%{_datadir}/siag/plugins/plugin.scm
%{_prefix}/man/man1/dummy_plugin.1

#%files siod not sure if should be subpackaged
%{_datadir}/siag/siod/siod.scm
%doc siod/docs/siod.html
%{_prefix}/man/man1/siod.1

#%files gvu
%attr(755,root,root) %{_bindir}/gvu
%doc gvu/README
%doc gvu/TODO
%{_prefix}/man/man1/gvu.1

#%files -n XawM  ?
#%{_libdir}/libXawM.so
#%{_libdir}/libXawM.so.0
#maybe it should be only this and in %%postin ldconfig -v?
%{_libdir}/libXawM.so.0.0.0
%doc XawM/README
%doc XawM/README.Linux
%doc XawM/README.XAW3D
%doc XawM/README.XawM
