Name:           afni
Version:        %{_afniver}
Release:        1%{?dist}
Summary:        Suite of image processing and statistical applications for neuroimaging.

License:        GPLv2+, Public Domain
URL:           	https://afni.nimh.nih.gov/
Source0:        https://afni.nimh.nih.gov/pub/dist/tgz/afni_src.tgz

Requires:	epel-release,tcsh,libXp,openmotif,gsl,xorg-x11-fonts-misc,PyQt4 R-devel,netpbm-progs,gnome-tweak-tool,ed,libpng12,xorg-x11-server-Xvfb,firefox
BuildRequires:  gcc,make,curl,tcsh
BuildArch:	x86_64

%description
AFNI is a set of C programs for processing, analyzing, and displaying functional MRI (FMRI) data - a technique for mapping human brain activity. It runs on Unix+X11+Motif systems, including SGI, Solaris, Linux, and Mac OS X. It is available free (in C source code format, and some precompiled binaries) for research purposes.


%install
cd %{buildroot}
curl -O https://afni.nimh.nih.gov/pub/dist/bin/linux_ubuntu_16_64/@update.afni.binaries
curl -O https://afni.nimh.nih.gov/pub/dist/tgz/linux_centos_7_64.tgz
tcsh @update.afni.binaries -local_package linux_centos_7_64.tgz -bindir %{buildroot}/usr/local/%{name} -apsearch yes
mkdir -p %{buildroot}/%{_sysconfdir}/profile.d
echo 'export PATH=/usr/local/bin/afni:${PATH}' > %{buildroot}/%{_sysconfdir}/profile.d/afni.sh
chmod 755  %{buildroot}/%{_sysconfdir}/profile.d/afni.sh
rm %{buildroot}/@update.afni.binaries
rm %{buildroot}/linux_centos_7_64.tgz

%files
/usr/local/%{name}
%{_sysconfdir}/profile.d/afni.sh

%changelog
* Mon Jan 21 2019 John Pellman <pellman.john@gmail.com> - %{_afniver}
- First AFNI package.
