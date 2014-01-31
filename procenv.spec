Name:           procenv
Version:        0.30
Release:        1%{?dist}
Summary:        Utility to show process environment

Group:          Applications/System
License:        GPLv3+
URL:            https://launchpad.net/procenv
Source0:        https://launchpad.net/procenv/trunk/%{version}/+download/procenv-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# fixme: should be autoconf >= 2.68, but Fedora packages or alien'ed dpkg
# need a later m4 too
BuildRequires:  gcc, make, binutils, autoconf, automake, pkgconfig

%description
This package contains a command-line tool that displays as much
detail about itself and its environment as possible. It can be
used as a test tool, to understand the type of environment a
process runs in, and for comparing system environments.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/procenv
%{_mandir}/man1/procenv.1.gz
%doc

%changelog
* Thu Jan 23 2014 James Hunt <james.hunt@ubuntu.com> - 0.30-1
- Update to 0.30.

* Wed Nov 14 2013 Dave Love <d.love@liverpool.ac.uk> - 0.27-1
- Update to 0.27, fix Source0

* Sun Dec  9 2012 Dave Love <fx@gnu.org> - 0.18-1
- Update to 0.18

* Tue Dec  4 2012 Dave Love <fx@gnu.org> - 0.16-2
- Re-fix locale-reporting.

* Mon Dec  3 2012 Dave Love <fx@gnu.org> - 0.16-1
- Update to 0.16

* Thu Nov 22 2012 Dave Love <fx@gnu.org> - 0.12-1
- Initial packaging