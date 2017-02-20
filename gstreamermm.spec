#
# Conditional build:
%bcond_without	static_libs	# static libraries
%bcond_without	gstpd		# gstreamer-plugins-bad library
%bcond_without	opengl		# gstreamer-gl library support (in plugins-bad library)
#
Summary:	A C++ bindings for the GStreamer library
Summary(pl.UTF-8):	Wiązania C++ do biblioteki GStreamera
Name:		gstreamermm
Version:	1.8.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gstreamermm/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	31246cf2f37b7ff48d45c8be98425e93
Patch0:		%{name}-link.patch
URL:		https://gstreamer.freedesktop.org/bindings/cplusplus.html
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	glibmm-devel >= 2.48.0
BuildRequires:	gstreamer-devel >= 1.8.0
%{?with_gstpd:BuildRequires:	gstreamer-plugins-bad-devel >= 1.8.0}
BuildRequires:	gstreamer-plugins-base-devel >= 1.8.0
# for not packaged examples only
#BuildRequires:	gtkmm3-devel >= 3.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:1.5
BuildRequires:	m4
BuildRequires:	mm-common >= 0.9.8
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glibmm >= 2.48.0
Requires:	gstreamer >= 1.8.0
Requires:	gstreamer-plugins-base >= 1.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gstreamermm provides C++ bindings for the GStreamer streaming
multimedia library. With gstreamermm it is possible to develop
applications that work with multimedia in C++.

%description -l pl.UTF-8
gstreamermm dostarcza wiązania C++ dla biblioteki strumieniowej
GStreamer. Za pomocą gstreamermm jest możliwe tworzenie aplikacji
multimedialnych w C++.

%package devel
Summary:	Header files for gstreamermm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gstreamermm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.48.0
Requires:	gstreamer-devel >= 1.8.0
Requires:	gstreamer-plugins-base-devel >= 1.8.0

%description devel
Header files for gstreamermm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gstreamermm.

%package static
Summary:	Static gstreamermm library
Summary(pl.UTF-8):	Biblioteka statyczna gstreamermm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gstreamermm library.

%description static -l pl.UTF-8
Biblioteka statyczna gstreamermm.

%package plugins-bad
Summary:	C++ bindings for the GStreamer plugins-bad library
Summary(pl.UTF-8):	Wiązania C++ do biblitoteki GStreamera plugins-bad
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer-plugins-bad >= 1.8.0

%description plugins-bad
C++ bindings for the GStreamer plugins-bad library.

%description plugins-bad -l pl.UTF-8
Wiązania C++ do biblitoteki GStreamera plugins-bad.

%package plugins-bad-devel
Summary:	Header files for gstreamermm-plugins-bad library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gstreamermm-plugins-bad
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-plugins-bad = %{version}-%{release}
Requires:	gstreamer-plugins-bad-devel >= 1.8.0

%description plugins-bad-devel
Header files for gstreamermm-plugins-bad library.

%description plugins-bad-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gstreamermm-plugins-bad.

%package plugins-bad-static
Summary:	Static gstreamermm-plugins-bad library
Summary(pl.UTF-8):	Biblioteka statyczna gstreamermm-plugins-bad
Group:		Development/Libraries
Requires:	%{name}-plugins-bad-devel = %{version}-%{release}

%description plugins-bad-static
Static gstreamermm-plugins-bad library.

%description plugins-bad-static -l pl.UTF-8
Biblioteka statyczna gstreamermm-plugins-bad.

%package doc
Summary:	Reference documentation for gstreamermm
Summary(pl.UTF-8):	Szczegółowa dokumentacja gstreamermm
Group:		Documentation
Requires:	devhelp

%description doc
Reference documentation for gstreamermm.

%description doc -l pl.UTF-8
Szczegółowa dokumentacja gstreamermm.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_opengl:--disable-gl} \
	%{!?with_gstpd:--disable-plugins-bad} \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgstreamermm*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   plugins-bad -p /sbin/ldconfig
%postun plugins-bad -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgstreamermm-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstreamermm-1.0.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstreamermm-1.0.so
%dir %{_libdir}/gstreamermm-1.0
%dir %{_libdir}/gstreamermm-1.0/gen
%attr(755,root,root) %{_libdir}/gstreamermm-1.0/gen/generate_plugin_gmmproc_file
%{_libdir}/gstreamermm-1.0/gen/m4
%{_libdir}/gstreamermm-1.0/include
%{_includedir}/gstreamermm-1.0
%{_pkgconfigdir}/gstreamermm-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgstreamermm-1.0.a
%endif

%if %{with gstpd}
%files plugins-bad
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstreamermm-plugins-bad-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstreamermm-plugins-bad-1.0.so.1

%files plugins-bad-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstreamermm-plugins-bad-1.0.so
%{_pkgconfigdir}/gstreamermm-plugins-bad-1.0.pc

%if %{with static_libs}
%files plugins-bad-static
%defattr(644,root,root,755)
%{_libdir}/libgstreamermm-plugins-bad-1.0.a
%endif
%endif

%files doc
%defattr(644,root,root,755)
%{_docdir}/gstreamermm-1.0
%{_datadir}/devhelp/books/gstreamermm-1.0
