Name:           xmltoman
Version:        0.4
Release:        4%{?dist}
Summary:        Scripts for converting XML to roff or HTML

Group:          Applications/Publishing
License:        GPLv2+
URL:            http://sourceforge.net/projects/xmltoman/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         xmltoman-0.3-timestamps.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  perl(XML::Parser)
BuildArch:      noarch

%description
This package provides xmltoman and xmlmantohtml scripts, to compile
the xml representation of manual page to either roff source, or HTML
(while providing the CSS stylesheet for eye-candy look). XSL stylesheet
for doing rougly the same job is provided.


%prep
%setup -q
%patch0 -p1 -b .timestamps


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/xmltoman
%{_bindir}/xmlmantohtml
%{_datadir}/xmltoman
%doc COPYING README


%changelog
* Tue Feb 23 2010 Ondrej Vasik <ovasik@redhat.com> - 0.4-4
- don't change target from "install" to "install -p"

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.4-3.1
- Rebuilt for RHEL 6

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May 29 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.4-1
- New upstream release

* Wed Mar 12 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.3-2
- Preserve timestamps, sanitize requires (thanks to Parag AN)

* Sun Mar 09 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.3-1
- Initial packaging attempt
