%define gstdir gstreamer-0.10

Name:           gstreamer-plugins-ugly
Version:        0.10.19
Release:        1%{?dist}
Summary:        GStreamer v0.x Ugly Plug-ins

License:        LGPLv2.1
URL:            https://gstreamer.freedesktop.org/modules/gst-plugins-ugly.html
Source0:        https://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-%{version}.tar.xz
Patch0:         0001-new-libcdio.patch
Patch1:         0002-new-opencore-amr.patch

BuildRequires:  gstreamer-devel >= 0.10
BuildRequires:  gstreamer-plugins-base-devel >= 0.10
BuildRequires:  gettext-devel
BuildRequires:  gtk-doc
BuildRequires:  orc-devel

BuildRequires:  liba52-devel
BuildRequires:  opencore-amr-devel
BuildRequires:  libcdio-devel
BuildRequires:  libdvdread-devel
BuildRequires:  libmp3lame-devel
BuildRequires:  libmad-devel
BuildRequires:  libmpeg2-devel
BuildRequires:  libtwolame-devel
BuildRequires:  libx264-devel

%description
GStreamer Ugly Plug-ins is a set of plug-ins that have good quality and correct
functionality, but distributing them might pose problems. The license on either
the plug-ins or the supporting libraries might not be how we'd like. The code
might be widely known to present patent problems.


# a52dec {{{
%package a52dec
Summary:        Decodes ATSC A/52 encoded audio streams
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description a52dec
%{summary}.
# }}}

# opencore-amr {{{
%package opencore-amr
Summary:        Adaptive Multi-Rate decoders and encoders
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description opencore-amr
%{summary}.
# }}}

# cdio {{{
%package cdio
Summary:        Read audio from audio CDs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description cdio
%{summary}.
# }}}

# dvdreadsrc {{{
%package dvdreadsrc
Summary:        Access a DVD title/chapter/angle using libdvdread
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description dvdreadsrc
%{summary}.
# }}}

# lame {{{
%package lame
Summary:        Encode MP3s with LAME
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description lame
%{summary}.
# }}}

# mad {{{
%package mad
Summary:        mp3 decoding based on the mad library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description mad
%{summary}.
# }}}

# mpeg2dec {{{
%package mpeg2dec
Summary:        Uses libmpeg2 to decode MPEG video streams
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description mpeg2dec
%{summary}.
# }}}

# twolame {{{
%package twolame
Summary:        Encode MP2s with TwoLAME
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description twolame
%{summary}.
# }}}

# x264 {{{
%package x264
Summary:        libx264-based H264 plugins
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description x264
%{summary}.
# }}}


%prep
%setup -q -n gst-plugins-ugly-%{version}
%patch0 -p1
%patch1 -p1


%build
%configure --disable-static --disable-silent-rules --enable-gtk-doc
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang gst-plugins-ugly-0.10


%files -f gst-plugins-ugly-0.10.lang
%license COPYING
%doc AUTHORS ChangeLog README
%doc %{_datadir}/gtk-doc/
%dir %{_datadir}/%{gstdir}/presets/
%{_libdir}/%{gstdir}/libgstasf.so
%{_libdir}/%{gstdir}/libgstdvdlpcmdec.so
%{_libdir}/%{gstdir}/libgstdvdsub.so
%{_libdir}/%{gstdir}/libgstrmdemux.so
%{_libdir}/%{gstdir}/libgstiec958.so
%{_libdir}/%{gstdir}/libgstmpegaudioparse.so
%{_libdir}/%{gstdir}/libgstmpegstream.so

%files a52dec
%{_libdir}/%{gstdir}/libgsta52dec.so

%files opencore-amr
%{_libdir}/%{gstdir}/libgstamrnb.so
%{_libdir}/%{gstdir}/libgstamrwbdec.so
%{_datadir}/%{gstdir}/presets/GstAmrnbEnc.prs

%files cdio
%{_libdir}/%{gstdir}/libgstcdio.so

%files dvdreadsrc
%{_libdir}/%{gstdir}/libgstdvdread.so

%files lame
%{_libdir}/%{gstdir}/libgstlame.so

%files mad
%{_libdir}/%{gstdir}/libgstmad.so

%files mpeg2dec
%{_libdir}/%{gstdir}/libgstmpeg2dec.so

%files twolame
%{_libdir}/%{gstdir}/libgsttwolame.so

%files x264
%{_libdir}/%{gstdir}/libgstx264.so
%{_datadir}/%{gstdir}/presets/GstX264Enc.prs


%changelog
* Mon May 16 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.10.19-1
- Public release

# vim: foldmethod=marker
