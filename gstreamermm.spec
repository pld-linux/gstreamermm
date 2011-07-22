#
# Conditional build:
%bcond_without  static_libs	# don't build static libraries
#
Summary:	A C++ bindings for the GStreamer library
Summary(pl.UTF-8):	Wiązania C++ do biblioteki GStreamera
Name:		gstreamermm
Version:	0.10.10
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gstreamermm/0.10/%{name}-%{version}.tar.bz2
# Source0-md5:	af6980a9526277b67df35a52b4e00bf4
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	glibmm-devel >= 2.28.0
BuildRequires:	gstreamer-devel >= 0.10.35
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.35
# for not packaged examples only
#BuildRequires:	gtkmm3-devel >= 3.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml++-devel >= 2.14
BuildRequires:	mm-common >= 0.9.5
BuildRequires:	pkgconfig
Requires:	glibmm >= 2.28.0
Requires:	gstreamer >= 0.10.35
Requires:	gstreamer-plugins-base >= 0.10.35
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
Summary:	gstreamermm header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gstreamermm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.28.0
Requires:	gstreamer-devel >= 0.10.35
Requires:	gstreamer-plugins-base-devel >= 0.10.35
Requires:	libxml++-devel >= 2.14

%description devel
Header files for gstreamermm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gstreamermm.

%package static
Summary:	gstreamermm static libraries
Summary(pl.UTF-8):	Biblioteki statyczne gstreamermm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
gstreamermm static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne gstreamermm.

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

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgstreamermm-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstreamermm-0.10.so.2
%attr(755,root,root) %{_libdir}/libgstreamermm_get_plugin_defs-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstreamermm_get_plugin_defs-0.10.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstreamermm-0.10.so
%attr(755,root,root) %{_libdir}/libgstreamermm_get_plugin_defs-0.10.so
%{_libdir}/libgstreamermm-0.10.la
%{_libdir}/libgstreamermm_get_plugin_defs-0.10.la
%{_libdir}/gstreamermm-0.10
%{_includedir}/gstreamermm-0.10
%{_pkgconfigdir}/gstreamermm-0.10.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgstreamermm-0.10.a
%{_libdir}/libgstreamermm_get_plugin_defs-0.10.a
%endif

%files doc
%defattr(644,root,root,755)
%{_docdir}/gstreamermm-0.10
%{_datadir}/devhelp/books/gstreamermm-0.10
