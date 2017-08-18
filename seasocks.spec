Name:           seasocks
Version:        1.3.1
Release:        1%{?dist}
Summary:        Simple, small, C++ embeddable webserver with WebSockets support

License:        BSD 2 Clause
URL:            https://github.com/mattgodbolt/seasocks
Source0:        https://github.com/mattgodbolt/seasocks/archive/v%{version}.tar.gz
Patch1:         so_version.patch

BuildRequires:  cmake3
BuildRequires:  zlib-devel

%description
Seasocks is a tiny embeddable C++ server with WebSockets support.

%package        devel
Summary:        Development files for %{name}

%description    devel
The %{name}-devel package contains the header files for developing applications
that use %{name}.

%prep
%setup -q
%patch1 -p0

%build
mkdir build
pushd build
  %cmake3 -DCMAKE_CXX_FLAGS="-g" ..
make %{?_smp_mflags}
popd

%install
pushd build
  %make_install
popd

%check
pushd build
  ctest3 -V %{?_smp_mflags}
popd

%files
%{_libdir}/libseasocks.so.%{version}

%files devel
%{_includedir}/seasocks/*
%{_libdir}/libseasocks.so
%{_libdir}/libseasocks.a

%changelog
* Thu Aug 17 2017 Viet The Nguyen <vnguyen@jpl.nasa.gov> - 1.3.1-1
- Initial packaging
