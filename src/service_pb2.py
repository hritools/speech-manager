# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rservice.proto\"\x14\n\x04Text\x12\x0c\n\x04text\x18\x01 \x01(\t\"\r\n\x0bTTSResponse2.\n\x0cTextToSpeech\x12\x1e\n\x05speak\x12\x05.Text\x1a\x0c.TTSResponse\"\x00\x62\x06proto3')
)




_TEXT = _descriptor.Descriptor(
  name='Text',
  full_name='Text',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='Text.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=37,
)


_TTSRESPONSE = _descriptor.Descriptor(
  name='TTSResponse',
  full_name='TTSResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=52,
)

DESCRIPTOR.message_types_by_name['Text'] = _TEXT
DESCRIPTOR.message_types_by_name['TTSResponse'] = _TTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Text = _reflection.GeneratedProtocolMessageType('Text', (_message.Message,), dict(
  DESCRIPTOR = _TEXT,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:Text)
  ))
_sym_db.RegisterMessage(Text)

TTSResponse = _reflection.GeneratedProtocolMessageType('TTSResponse', (_message.Message,), dict(
  DESCRIPTOR = _TTSRESPONSE,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:TTSResponse)
  ))
_sym_db.RegisterMessage(TTSResponse)



_TEXTTOSPEECH = _descriptor.ServiceDescriptor(
  name='TextToSpeech',
  full_name='TextToSpeech',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=54,
  serialized_end=100,
  methods=[
  _descriptor.MethodDescriptor(
    name='speak',
    full_name='TextToSpeech.speak',
    index=0,
    containing_service=None,
    input_type=_TEXT,
    output_type=_TTSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEXTTOSPEECH)

DESCRIPTOR.services_by_name['TextToSpeech'] = _TEXTTOSPEECH

# @@protoc_insertion_point(module_scope)
