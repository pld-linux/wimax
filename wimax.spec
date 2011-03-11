Summary:	WiMAX Network Service for the Intel 2400m
Name:		wimax
Version:	1.5.1
Release:	1
License:	BSD
Group:		Libraries
# http://www.linuxwimax.org/Download
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	8d7fae21a62b5aeda3f730c484bdd5fb
Patch0:		%{name}-link.patch
URL:		http://www.linuxwimax.org/
BuildRequires:	libeap-devel >= 0.7.0
BuildRequires:	libwimaxll-devel
BuildRequires:	linux-libc-headers
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
User space daemon for the Intel 2400m Wireless WiMAX Link. This daemon
takes care of handling network scan, discovery and management.

%package libs
Summary:	WiMAX Network Service libraries
Summary(pl.UTF-8):	Biblioteki WiMAX Network Service
Group:		Libraries

%description libs
WiMAX Network Service libraries.

%description libs -l pl.UTF-8
Biblioteki WiMAX Network Service.

%package devel
Summary:	Header files for WiMAX Network Service libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek WiMAX Network Service
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for WiMAX Network Service libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek WiMAX Network Service.

%package static
Summary:	Static WiMAX Network Service libraries
Summary(pl.UTF-8):	Statyczne biblioteki WiMAX Network Service
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WiMAX Network Service libraries.

%description static -l pl.UTF-8
Statyczne biblioteki WiMAX Network Service.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun libs	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wimax_monitor
%attr(755,root,root) %{_bindir}/wimaxcu
%attr(755,root,root) %{_bindir}/wimaxd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/wimax.conf
%config(noreplace) %verify(not md5 mtime size) /etc/modprobe.d/i2400m.conf
%config(noreplace) %verify(not md5 mtime size) /etc/udev/rules.d/iwmxsdk.rules
%dir %{_sysconfdir}/wimax
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/wimax/config.xml
%{_datadir}/wimax
%{_mandir}/man1/wimaxcu.1*
%{_mandir}/man1/wimaxd.1*
%dir /var/lib/wimax
/var/lib/wimax/WiMAX_DB.bin
/var/lib/wimax/WiMAX_Def.bin

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libWmxInstrument.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libWmxInstrument.so.0
%attr(755,root,root) %{_libdir}/libiWmxSdk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libiWmxSdk.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libWmxInstrument.so
%attr(755,root,root) %{_libdir}/libiWmxSdk.so
%{_includedir}/wimax
%{_pkgconfigdir}/libiWmxSdk-0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libWmxInstrument.a
%{_libdir}/libiWmxSdk.a
