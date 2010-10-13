#
# Conditional build:
%bcond_without  static_libs	# don't build static libraries
#
Summary:	A C++ bindings for the GStreamer
Summary(pl.UTF-8):	Wiązania C++ dla GStreamer
Name:		gstreamermm
Version:	0.10.7.3
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gstreamermm/0.10/%{name}-%{version}.tar.bz2
# Source0-md5:	48df9161cec157cd74c2aac0d97d2c0f
Patch0:		%{name}-gcc45.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibmm-devel >= 2.18.1
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0
BuildRequires:	gtkmm-devel >= 2.12.0
BuildRequires:	libxml++-devel >= 2.14.0
BuildRequires:	pkgconfig
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
Summary(pl.UTF-8):	Pliki nagłówkowe gstreamermm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gstreamermm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gstreamermm.

%package doc
Summary:	Reference documentation for gstreamermm
Summary(pl.UTF-8):	Szczegółowa dokumentacja gstreamermm
Group:		Documentation
Requires:	devhelp

%description doc
Reference documentation for gstreamermm.

%description doc -l pl.UTF-8
Szczegółowa dokumentacja gstreamermm.

%package static
Summary:	gstreamermm static libraries
Summary(pl.UTF-8):	Biblioteki statyczne gstreamermm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
gstreamermm static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne gstreamermm.

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

%files doc
%defattr(644,root,root,755)
%{_docdir}/gstreamermm-0.10
%{_datadir}/devhelp/books/gstreamermm-0.10

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgstreamermm-0.10.a
%{_libdir}/libgstreamermm_get_plugin_defs-0.10.a
%endif
