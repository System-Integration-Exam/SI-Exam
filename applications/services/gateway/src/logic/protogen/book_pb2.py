# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="book.proto",
    package="",
    syntax="proto3",
    serialized_options=b"\252\002\017Metadata.Protos",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\nbook.proto"B\n\x11\x43reateBookRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\x12\x0e\n\x06rating\x18\x03 \x01(\x05"0\n\x12\x43reateBookResponse\x12\x1a\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x0c.BookMessage" \n\x12GetBookByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t"P\n\x13GetBookByIdResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x0e\n\x06rating\x18\x04 \x01(\x05"N\n\x11UpdateBookRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x0e\n\x06rating\x18\x04 \x01(\x05"+\n\x12UpdateBookResponse\x12\x15\n\rstatusMessage\x18\x01 \x01(\t"#\n\x15\x44\x65leteBookByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t"/\n\x16\x44\x65leteBookByIdResponse\x12\x15\n\rstatusMessage\x18\x01 \x01(\t"\x14\n\x12GetAllBooksRequest"2\n\x13GetAllBooksResponse\x12\x1b\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\x0c.BookMessage"H\n\x0b\x42ookMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x0e\n\x06rating\x18\x04 \x01(\x05\x32\xb5\x02\n\x04\x42ook\x12\x37\n\ncreateBook\x12\x12.CreateBookRequest\x1a\x13.CreateBookResponse"\x00\x12:\n\x0bgetBookById\x12\x13.GetBookByIdRequest\x1a\x14.GetBookByIdResponse"\x00\x12\x37\n\nupdateBook\x12\x12.UpdateBookRequest\x1a\x13.UpdateBookResponse"\x00\x12\x43\n\x0e\x64\x65leteBookById\x12\x16.DeleteBookByIdRequest\x1a\x17.DeleteBookByIdResponse"\x00\x12:\n\x0bgetAllBooks\x12\x13.GetAllBooksRequest\x1a\x14.GetAllBooksResponse"\x00\x42\x12\xaa\x02\x0fMetadata.Protosb\x06proto3',
)


_CREATEBOOKREQUEST = _descriptor.Descriptor(
    name="CreateBookRequest",
    full_name="CreateBookRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="title",
            full_name="CreateBookRequest.title",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="author",
            full_name="CreateBookRequest.author",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="rating",
            full_name="CreateBookRequest.rating",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=14,
    serialized_end=80,
)


_CREATEBOOKRESPONSE = _descriptor.Descriptor(
    name="CreateBookResponse",
    full_name="CreateBookResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="book",
            full_name="CreateBookResponse.book",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=82,
    serialized_end=130,
)


_GETBOOKBYIDREQUEST = _descriptor.Descriptor(
    name="GetBookByIdRequest",
    full_name="GetBookByIdRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="GetBookByIdRequest.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=132,
    serialized_end=164,
)


_GETBOOKBYIDRESPONSE = _descriptor.Descriptor(
    name="GetBookByIdResponse",
    full_name="GetBookByIdResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="GetBookByIdResponse.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="title",
            full_name="GetBookByIdResponse.title",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="author",
            full_name="GetBookByIdResponse.author",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="rating",
            full_name="GetBookByIdResponse.rating",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=166,
    serialized_end=246,
)


_UPDATEBOOKREQUEST = _descriptor.Descriptor(
    name="UpdateBookRequest",
    full_name="UpdateBookRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="UpdateBookRequest.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="title",
            full_name="UpdateBookRequest.title",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="author",
            full_name="UpdateBookRequest.author",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="rating",
            full_name="UpdateBookRequest.rating",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=248,
    serialized_end=326,
)


_UPDATEBOOKRESPONSE = _descriptor.Descriptor(
    name="UpdateBookResponse",
    full_name="UpdateBookResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="statusMessage",
            full_name="UpdateBookResponse.statusMessage",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=328,
    serialized_end=371,
)


_DELETEBOOKBYIDREQUEST = _descriptor.Descriptor(
    name="DeleteBookByIdRequest",
    full_name="DeleteBookByIdRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="DeleteBookByIdRequest.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=373,
    serialized_end=408,
)


_DELETEBOOKBYIDRESPONSE = _descriptor.Descriptor(
    name="DeleteBookByIdResponse",
    full_name="DeleteBookByIdResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="statusMessage",
            full_name="DeleteBookByIdResponse.statusMessage",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=410,
    serialized_end=457,
)


_GETALLBOOKSREQUEST = _descriptor.Descriptor(
    name="GetAllBooksRequest",
    full_name="GetAllBooksRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=459,
    serialized_end=479,
)


_GETALLBOOKSRESPONSE = _descriptor.Descriptor(
    name="GetAllBooksResponse",
    full_name="GetAllBooksResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="books",
            full_name="GetAllBooksResponse.books",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=481,
    serialized_end=531,
)


_BOOKMESSAGE = _descriptor.Descriptor(
    name="BookMessage",
    full_name="BookMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="BookMessage.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="title",
            full_name="BookMessage.title",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="author",
            full_name="BookMessage.author",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="rating",
            full_name="BookMessage.rating",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=533,
    serialized_end=605,
)

_CREATEBOOKRESPONSE.fields_by_name["book"].message_type = _BOOKMESSAGE
_GETALLBOOKSRESPONSE.fields_by_name["books"].message_type = _BOOKMESSAGE
DESCRIPTOR.message_types_by_name["CreateBookRequest"] = _CREATEBOOKREQUEST
DESCRIPTOR.message_types_by_name["CreateBookResponse"] = _CREATEBOOKRESPONSE
DESCRIPTOR.message_types_by_name["GetBookByIdRequest"] = _GETBOOKBYIDREQUEST
DESCRIPTOR.message_types_by_name["GetBookByIdResponse"] = _GETBOOKBYIDRESPONSE
DESCRIPTOR.message_types_by_name["UpdateBookRequest"] = _UPDATEBOOKREQUEST
DESCRIPTOR.message_types_by_name["UpdateBookResponse"] = _UPDATEBOOKRESPONSE
DESCRIPTOR.message_types_by_name["DeleteBookByIdRequest"] = _DELETEBOOKBYIDREQUEST
DESCRIPTOR.message_types_by_name["DeleteBookByIdResponse"] = _DELETEBOOKBYIDRESPONSE
DESCRIPTOR.message_types_by_name["GetAllBooksRequest"] = _GETALLBOOKSREQUEST
DESCRIPTOR.message_types_by_name["GetAllBooksResponse"] = _GETALLBOOKSRESPONSE
DESCRIPTOR.message_types_by_name["BookMessage"] = _BOOKMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateBookRequest = _reflection.GeneratedProtocolMessageType(
    "CreateBookRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEBOOKREQUEST,
        "__module__": "book_pb2"
        # @@protoc_insertion_point(class_scope:CreateBookRequest)
    },
)
_sym_db.RegisterMessage(CreateBookRequest)

CreateBookResponse = _reflection.GeneratedProtocolMessageType(
    "CreateBookResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEBOOKRESPONSE,
        "__module__": "book_pb2"
        # @@protoc_insertion_point(class_scope:CreateBookResponse)
    },
)
_sym_db.RegisterMessage(CreateBookResponse)

GetBookByIdRequest = _reflection.GeneratedProtocolMessageType(
    "GetBookByIdRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETBOOKBYIDREQUEST,
        "__module__": "book_pb2"
        # @@protoc_insertion_point(class_scope:GetBookByIdRequest)
    },
)
_sym_db.RegisterMessage(GetBookByIdRequest)

GetBookByIdResponse = _reflection.GeneratedProtocolMessageType(
    "GetBookByIdResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETBOOKBYIDRESPONSE,
        "__module__": "book_pb2"
        # @@protoc_insertion_point(class_scope:GetBookByIdResponse)
    },
)
_sym_db.RegisterMessage(GetBookByIdResponse)

UpdateBookRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateBookRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEBOOKREQUEST,
        "__module__": "book_pb2"
        # @@protoc_insertion_point(class_scope:UpdateBookRequest)
    },
)
_sym_db.RegisterMessage(UpdateBookRequest)

UpdateBookResponse = _reflection.GeneratedProtocolMessageType(
    "UpdateBookResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEBOOKRESPONSE,
        "__module__": "book_pb2"
        # @@protoc_insertion_point(class_scope:UpdateBookResponse)
    },
)
_sym_db.RegisterMessage(UpdateBookResponse)

DeleteBookByIdRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteBookByIdRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETEBOOKBYIDREQUEST,
        "__module__": "book_pb2"
        # @@protoc_insertion_point(class_scope:DeleteBookByIdRequest)
    },
)
_sym_db.RegisterMessage(DeleteBookByIdRequest)

DeleteBookByIdResponse = _reflection.GeneratedProtocolMessageType(
    "DeleteBookByIdResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETEBOOKBYIDRESPONSE,
        "__module__": "book_pb2"
        # @@protoc_insertion_point(class_scope:DeleteBookByIdResponse)
    },
)
_sym_db.RegisterMessage(DeleteBookByIdResponse)

GetAllBooksRequest = _reflection.GeneratedProtocolMessageType(
    "GetAllBooksRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETALLBOOKSREQUEST,
        "__module__": "book_pb2"
        # @@protoc_insertion_point(class_scope:GetAllBooksRequest)
    },
)
_sym_db.RegisterMessage(GetAllBooksRequest)

GetAllBooksResponse = _reflection.GeneratedProtocolMessageType(
    "GetAllBooksResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETALLBOOKSRESPONSE,
        "__module__": "book_pb2"
        # @@protoc_insertion_point(class_scope:GetAllBooksResponse)
    },
)
_sym_db.RegisterMessage(GetAllBooksResponse)

BookMessage = _reflection.GeneratedProtocolMessageType(
    "BookMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _BOOKMESSAGE,
        "__module__": "book_pb2"
        # @@protoc_insertion_point(class_scope:BookMessage)
    },
)
_sym_db.RegisterMessage(BookMessage)


DESCRIPTOR._options = None

_BOOK = _descriptor.ServiceDescriptor(
    name="Book",
    full_name="Book",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=608,
    serialized_end=917,
    methods=[
        _descriptor.MethodDescriptor(
            name="createBook",
            full_name="Book.createBook",
            index=0,
            containing_service=None,
            input_type=_CREATEBOOKREQUEST,
            output_type=_CREATEBOOKRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="getBookById",
            full_name="Book.getBookById",
            index=1,
            containing_service=None,
            input_type=_GETBOOKBYIDREQUEST,
            output_type=_GETBOOKBYIDRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="updateBook",
            full_name="Book.updateBook",
            index=2,
            containing_service=None,
            input_type=_UPDATEBOOKREQUEST,
            output_type=_UPDATEBOOKRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="deleteBookById",
            full_name="Book.deleteBookById",
            index=3,
            containing_service=None,
            input_type=_DELETEBOOKBYIDREQUEST,
            output_type=_DELETEBOOKBYIDRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="getAllBooks",
            full_name="Book.getAllBooks",
            index=4,
            containing_service=None,
            input_type=_GETALLBOOKSREQUEST,
            output_type=_GETALLBOOKSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_BOOK)

DESCRIPTOR.services_by_name["Book"] = _BOOK

# @@protoc_insertion_point(module_scope)
