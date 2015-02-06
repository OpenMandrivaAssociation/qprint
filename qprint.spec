Summary:	Encode and decode quoted printable data
Name:           qprint
Version:        1.0
Release:        10
License:        Public Domain
Group:		Networking/Mail
URL:		http://www.fourmilab.ch/webtools/qprint/
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
qprint is a command line utility which encodes and decodes
files in this format. It can be used within a pipeline as
an encoding or decoding filter, and is most commonly used
in this manner as part of an automated mail processing
system. With appropriate options, qprint can encode pure
binary files, but it's a poor choice since it may inflate
the size of the file by as much as a factor of three. The
base64 MIME encoding is a better choice for such data. 

%prep

%setup -q

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m755 qprint %{buildroot}%{_bindir}/
install -m755 qprint.1 %{buildroot}%{_mandir}/man1/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README index.html logo.gif qprint.pdf rfc1521.*
%{_bindir}/qprint
%{_mandir}/man1/qprint.1*


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0-9mdv2010.0
+ Revision: 433040
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-8mdv2009.0
+ Revision: 242502
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Aug 19 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2008.0
+ Revision: 66674
- Import qprint



* Fri Jul 14 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2007.0
- rebuild

* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdk
- rebuild

* Sun May 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-4mdk
- use macros

* Thu Jan 16 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.0-3mdk
- build release

* Wed Jun 12 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.0-2mdk
- fix Requires (to null)

* Wed Jun 12 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.0-1mdk
- initial cooker contrib
