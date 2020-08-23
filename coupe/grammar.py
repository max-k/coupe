# flake8: noqa
GRAMMAR = """
CueSheet:
    commands+=Command
;

Command:
    REM | AlbumTag | MetaTag | File
;

REM:
    'REM' REMComment
;

REMComment:
    REMDate | REMDiscId | REMIdOrString
;

REMDate:
    name='DATE' value=/(?:19|20)\d{2}/
;

REMDiscId:
    name='DISCID' value=/[0-9A-F]{8}/
;

REMIdOrString:
    name=REMName value=IdOrString
;

REMName:
    'COMMENT' | 'GENRE'
;

IdOrString:
    ID | STRING
;

AlbumTag:
    Catalog | CdTextFile
;

Catalog:
    name='CATALOG' value=/\d{13}/
;

CdTextFile:
    name='CDTEXTFILE' value=IdOrString
;

MetaTag:
    name=MetaTagName value=IdOrString
;

MetaTagName:
    'PERFORMER' | 'SONGWRITER' | 'TITLE'
;

File:
    'FILE' name=STRING filetype=FileType tracks+=Track
;

FileType:
    'BINARY' | 'MOTOROLA' | 'AIFF' | 'WAVE' | 'MP3';

Track:
    'TRACK' number=TrackNumber datatype=DataType
    infos*=TrackInfo (pregap=PreGap)? indexes+=Index (postgap=PostGap)?
;

TrackNumber:
    /0[1-9]/ | /[1-9][0-9]/
;

DataType:
'AUDIO' | 'CDG' | 'MODE1/2048' | 'MODE1/2352' | 'MODE2/2336' | 'MODE2/2352' |
'CDI/2336' | 'CDI/2352'
;

TrackInfo:
    FlagList | Isrc | MetaTag
;

FlagList:
    name='FLAGS' values+=FlagValue[eolterm]
;

FlagValue:
    'DCP' | '4CH' | 'PRE' | 'DATA'
;

Isrc:
    name='ISRC' value=/([a-z]|[A-Z]){2}([a-z]|[A-Z]|[0-9]){3}[0-9]{7}/
;

PreGap:
    'PREGAP' timestamp=TimeStamp
;

Index:
    'INDEX' number=IndexNumber timestamp=TimeStamp
;

IndexNumber:
    /[0-9][0-9]/
;

PostGap:
    'POSTGAP' timestamp=TimeStamp
;

TimeStamp:
    minute=Time ':' second=Time ':' frame=Frame
;

Time:
    /[0-5][0-9]/
;

Frame:
    /[0-6][0-9]/ | /7[0-4]/
;
"""
