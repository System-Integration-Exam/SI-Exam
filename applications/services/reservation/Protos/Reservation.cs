// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: reservation.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Reservation.Protos {

  /// <summary>Holder for reflection information generated from reservation.proto</summary>
  public static partial class ReservationReflection {

    #region Descriptor
    /// <summary>File descriptor for reservation.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static ReservationReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "ChFyZXNlcnZhdGlvbi5wcm90bxILcmVzZXJ2YXRpb24iWwoNQ3JlYXRlUmVx",
            "ZXVzdBIPCgdpdGVtX2lkGAEgASgJEg8KB3VzZXJfaWQYAiABKAkSKAoLaXRl",
            "bV9mb3JtYXQYAyABKA4yEy5yZXNlcnZhdGlvbi5Gb3JtYXQiGwoNQ2hhbmdl",
            "UmVxZXVzdBIKCgJpZBgBIAEoCSIhCg5SZXRyaXZlUmVxdWVzdBIPCgd1c2Vy",
            "X2lkGAEgASgJIocBChNSZXNlcnZhdGlvblJlc3BvbnNlEgoKAmlkGAEgASgJ",
            "Eg8KB2l0ZW1faWQYAiABKAkSDwoHdXNlcl9pZBgDIAEoCRIoCgtpdGVtX2Zv",
            "cm1hdBgEIAEoDjITLnJlc2VydmF0aW9uLkZvcm1hdBIYChBleHBpcnlfdGlt",
            "ZV91bml4GAUgASgJIkkKD1JldHJpdmVSZXNwb25zZRI2CgxyZXNlcnZhdGlv",
            "bnMYASADKAsyIC5yZXNlcnZhdGlvbi5SZXNlcnZhdGlvblJlc3BvbnNlKicK",
            "BkZvcm1hdBIICgROVUxMEAASCAoEQk9PSxABEgkKBVZJTllMEAIy5wIKD1Jl",
            "c2VydmF0aW9uR3JwYxJRChFDcmVhdGVSZXNlcnZhdGlvbhIaLnJlc2VydmF0",
            "aW9uLkNyZWF0ZVJlcWV1c3QaIC5yZXNlcnZhdGlvbi5SZXNlcnZhdGlvblJl",
            "c3BvbnNlElEKEUNhbmNlbFJlc2VydmF0aW9uEhoucmVzZXJ2YXRpb24uQ2hh",
            "bmdlUmVxZXVzdBogLnJlc2VydmF0aW9uLlJlc2VydmF0aW9uUmVzcG9uc2US",
            "UwoTQ29tcGxldGVSZXNlcnZhdGlvbhIaLnJlc2VydmF0aW9uLkNoYW5nZVJl",
            "cWV1c3QaIC5yZXNlcnZhdGlvbi5SZXNlcnZhdGlvblJlc3BvbnNlElkKGFJl",
            "dHJpdmVVc2Vyc1Jlc2VydmF0aW9ucxIbLnJlc2VydmF0aW9uLlJldHJpdmVS",
            "ZXF1ZXN0GiAucmVzZXJ2YXRpb24uUmVzZXJ2YXRpb25SZXNwb25zZUIVqgIS",
            "UmVzZXJ2YXRpb24uUHJvdG9zYgZwcm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(new[] {typeof(global::Reservation.Protos.Format), }, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Reservation.Protos.CreateReqeust), global::Reservation.Protos.CreateReqeust.Parser, new[]{ "ItemId", "UserId", "ItemFormat" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Reservation.Protos.ChangeReqeust), global::Reservation.Protos.ChangeReqeust.Parser, new[]{ "Id" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Reservation.Protos.RetriveRequest), global::Reservation.Protos.RetriveRequest.Parser, new[]{ "UserId" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Reservation.Protos.ReservationResponse), global::Reservation.Protos.ReservationResponse.Parser, new[]{ "Id", "ItemId", "UserId", "ItemFormat", "ExpiryTimeUnix" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Reservation.Protos.RetriveResponse), global::Reservation.Protos.RetriveResponse.Parser, new[]{ "Reservations" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Enums
  public enum Format {
    [pbr::OriginalName("NULL")] Null = 0,
    [pbr::OriginalName("BOOK")] Book = 1,
    [pbr::OriginalName("VINYL")] Vinyl = 2,
  }

  #endregion

  #region Messages
  public sealed partial class CreateReqeust : pb::IMessage<CreateReqeust>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<CreateReqeust> _parser = new pb::MessageParser<CreateReqeust>(() => new CreateReqeust());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<CreateReqeust> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Reservation.Protos.ReservationReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public CreateReqeust() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public CreateReqeust(CreateReqeust other) : this() {
      itemId_ = other.itemId_;
      userId_ = other.userId_;
      itemFormat_ = other.itemFormat_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public CreateReqeust Clone() {
      return new CreateReqeust(this);
    }

    /// <summary>Field number for the "item_id" field.</summary>
    public const int ItemIdFieldNumber = 1;
    private string itemId_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string ItemId {
      get { return itemId_; }
      set {
        itemId_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "user_id" field.</summary>
    public const int UserIdFieldNumber = 2;
    private string userId_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string UserId {
      get { return userId_; }
      set {
        userId_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "item_format" field.</summary>
    public const int ItemFormatFieldNumber = 3;
    private global::Reservation.Protos.Format itemFormat_ = global::Reservation.Protos.Format.Null;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Reservation.Protos.Format ItemFormat {
      get { return itemFormat_; }
      set {
        itemFormat_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as CreateReqeust);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(CreateReqeust other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (ItemId != other.ItemId) return false;
      if (UserId != other.UserId) return false;
      if (ItemFormat != other.ItemFormat) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (ItemId.Length != 0) hash ^= ItemId.GetHashCode();
      if (UserId.Length != 0) hash ^= UserId.GetHashCode();
      if (ItemFormat != global::Reservation.Protos.Format.Null) hash ^= ItemFormat.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (ItemId.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(ItemId);
      }
      if (UserId.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(UserId);
      }
      if (ItemFormat != global::Reservation.Protos.Format.Null) {
        output.WriteRawTag(24);
        output.WriteEnum((int) ItemFormat);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (ItemId.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(ItemId);
      }
      if (UserId.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(UserId);
      }
      if (ItemFormat != global::Reservation.Protos.Format.Null) {
        output.WriteRawTag(24);
        output.WriteEnum((int) ItemFormat);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (ItemId.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(ItemId);
      }
      if (UserId.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(UserId);
      }
      if (ItemFormat != global::Reservation.Protos.Format.Null) {
        size += 1 + pb::CodedOutputStream.ComputeEnumSize((int) ItemFormat);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(CreateReqeust other) {
      if (other == null) {
        return;
      }
      if (other.ItemId.Length != 0) {
        ItemId = other.ItemId;
      }
      if (other.UserId.Length != 0) {
        UserId = other.UserId;
      }
      if (other.ItemFormat != global::Reservation.Protos.Format.Null) {
        ItemFormat = other.ItemFormat;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            ItemId = input.ReadString();
            break;
          }
          case 18: {
            UserId = input.ReadString();
            break;
          }
          case 24: {
            ItemFormat = (global::Reservation.Protos.Format) input.ReadEnum();
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            ItemId = input.ReadString();
            break;
          }
          case 18: {
            UserId = input.ReadString();
            break;
          }
          case 24: {
            ItemFormat = (global::Reservation.Protos.Format) input.ReadEnum();
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class ChangeReqeust : pb::IMessage<ChangeReqeust>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<ChangeReqeust> _parser = new pb::MessageParser<ChangeReqeust>(() => new ChangeReqeust());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<ChangeReqeust> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Reservation.Protos.ReservationReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ChangeReqeust() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ChangeReqeust(ChangeReqeust other) : this() {
      id_ = other.id_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ChangeReqeust Clone() {
      return new ChangeReqeust(this);
    }

    /// <summary>Field number for the "id" field.</summary>
    public const int IdFieldNumber = 1;
    private string id_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string Id {
      get { return id_; }
      set {
        id_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as ChangeReqeust);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(ChangeReqeust other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Id != other.Id) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Id.Length != 0) hash ^= Id.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (Id.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Id);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (Id.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Id);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (Id.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Id);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(ChangeReqeust other) {
      if (other == null) {
        return;
      }
      if (other.Id.Length != 0) {
        Id = other.Id;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            Id = input.ReadString();
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            Id = input.ReadString();
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class RetriveRequest : pb::IMessage<RetriveRequest>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<RetriveRequest> _parser = new pb::MessageParser<RetriveRequest>(() => new RetriveRequest());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<RetriveRequest> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Reservation.Protos.ReservationReflection.Descriptor.MessageTypes[2]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public RetriveRequest() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public RetriveRequest(RetriveRequest other) : this() {
      userId_ = other.userId_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public RetriveRequest Clone() {
      return new RetriveRequest(this);
    }

    /// <summary>Field number for the "user_id" field.</summary>
    public const int UserIdFieldNumber = 1;
    private string userId_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string UserId {
      get { return userId_; }
      set {
        userId_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as RetriveRequest);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(RetriveRequest other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (UserId != other.UserId) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (UserId.Length != 0) hash ^= UserId.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (UserId.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(UserId);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (UserId.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(UserId);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (UserId.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(UserId);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(RetriveRequest other) {
      if (other == null) {
        return;
      }
      if (other.UserId.Length != 0) {
        UserId = other.UserId;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            UserId = input.ReadString();
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            UserId = input.ReadString();
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class ReservationResponse : pb::IMessage<ReservationResponse>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<ReservationResponse> _parser = new pb::MessageParser<ReservationResponse>(() => new ReservationResponse());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<ReservationResponse> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Reservation.Protos.ReservationReflection.Descriptor.MessageTypes[3]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ReservationResponse() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ReservationResponse(ReservationResponse other) : this() {
      id_ = other.id_;
      itemId_ = other.itemId_;
      userId_ = other.userId_;
      itemFormat_ = other.itemFormat_;
      expiryTimeUnix_ = other.expiryTimeUnix_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ReservationResponse Clone() {
      return new ReservationResponse(this);
    }

    /// <summary>Field number for the "id" field.</summary>
    public const int IdFieldNumber = 1;
    private string id_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string Id {
      get { return id_; }
      set {
        id_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "item_id" field.</summary>
    public const int ItemIdFieldNumber = 2;
    private string itemId_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string ItemId {
      get { return itemId_; }
      set {
        itemId_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "user_id" field.</summary>
    public const int UserIdFieldNumber = 3;
    private string userId_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string UserId {
      get { return userId_; }
      set {
        userId_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "item_format" field.</summary>
    public const int ItemFormatFieldNumber = 4;
    private global::Reservation.Protos.Format itemFormat_ = global::Reservation.Protos.Format.Null;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Reservation.Protos.Format ItemFormat {
      get { return itemFormat_; }
      set {
        itemFormat_ = value;
      }
    }

    /// <summary>Field number for the "expiry_time_unix" field.</summary>
    public const int ExpiryTimeUnixFieldNumber = 5;
    private string expiryTimeUnix_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string ExpiryTimeUnix {
      get { return expiryTimeUnix_; }
      set {
        expiryTimeUnix_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as ReservationResponse);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(ReservationResponse other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Id != other.Id) return false;
      if (ItemId != other.ItemId) return false;
      if (UserId != other.UserId) return false;
      if (ItemFormat != other.ItemFormat) return false;
      if (ExpiryTimeUnix != other.ExpiryTimeUnix) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Id.Length != 0) hash ^= Id.GetHashCode();
      if (ItemId.Length != 0) hash ^= ItemId.GetHashCode();
      if (UserId.Length != 0) hash ^= UserId.GetHashCode();
      if (ItemFormat != global::Reservation.Protos.Format.Null) hash ^= ItemFormat.GetHashCode();
      if (ExpiryTimeUnix.Length != 0) hash ^= ExpiryTimeUnix.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (Id.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Id);
      }
      if (ItemId.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(ItemId);
      }
      if (UserId.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(UserId);
      }
      if (ItemFormat != global::Reservation.Protos.Format.Null) {
        output.WriteRawTag(32);
        output.WriteEnum((int) ItemFormat);
      }
      if (ExpiryTimeUnix.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(ExpiryTimeUnix);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (Id.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Id);
      }
      if (ItemId.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(ItemId);
      }
      if (UserId.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(UserId);
      }
      if (ItemFormat != global::Reservation.Protos.Format.Null) {
        output.WriteRawTag(32);
        output.WriteEnum((int) ItemFormat);
      }
      if (ExpiryTimeUnix.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(ExpiryTimeUnix);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (Id.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Id);
      }
      if (ItemId.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(ItemId);
      }
      if (UserId.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(UserId);
      }
      if (ItemFormat != global::Reservation.Protos.Format.Null) {
        size += 1 + pb::CodedOutputStream.ComputeEnumSize((int) ItemFormat);
      }
      if (ExpiryTimeUnix.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(ExpiryTimeUnix);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(ReservationResponse other) {
      if (other == null) {
        return;
      }
      if (other.Id.Length != 0) {
        Id = other.Id;
      }
      if (other.ItemId.Length != 0) {
        ItemId = other.ItemId;
      }
      if (other.UserId.Length != 0) {
        UserId = other.UserId;
      }
      if (other.ItemFormat != global::Reservation.Protos.Format.Null) {
        ItemFormat = other.ItemFormat;
      }
      if (other.ExpiryTimeUnix.Length != 0) {
        ExpiryTimeUnix = other.ExpiryTimeUnix;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            Id = input.ReadString();
            break;
          }
          case 18: {
            ItemId = input.ReadString();
            break;
          }
          case 26: {
            UserId = input.ReadString();
            break;
          }
          case 32: {
            ItemFormat = (global::Reservation.Protos.Format) input.ReadEnum();
            break;
          }
          case 42: {
            ExpiryTimeUnix = input.ReadString();
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            Id = input.ReadString();
            break;
          }
          case 18: {
            ItemId = input.ReadString();
            break;
          }
          case 26: {
            UserId = input.ReadString();
            break;
          }
          case 32: {
            ItemFormat = (global::Reservation.Protos.Format) input.ReadEnum();
            break;
          }
          case 42: {
            ExpiryTimeUnix = input.ReadString();
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class RetriveResponse : pb::IMessage<RetriveResponse>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<RetriveResponse> _parser = new pb::MessageParser<RetriveResponse>(() => new RetriveResponse());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<RetriveResponse> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Reservation.Protos.ReservationReflection.Descriptor.MessageTypes[4]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public RetriveResponse() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public RetriveResponse(RetriveResponse other) : this() {
      reservations_ = other.reservations_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public RetriveResponse Clone() {
      return new RetriveResponse(this);
    }

    /// <summary>Field number for the "reservations" field.</summary>
    public const int ReservationsFieldNumber = 1;
    private static readonly pb::FieldCodec<global::Reservation.Protos.ReservationResponse> _repeated_reservations_codec
        = pb::FieldCodec.ForMessage(10, global::Reservation.Protos.ReservationResponse.Parser);
    private readonly pbc::RepeatedField<global::Reservation.Protos.ReservationResponse> reservations_ = new pbc::RepeatedField<global::Reservation.Protos.ReservationResponse>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::Reservation.Protos.ReservationResponse> Reservations {
      get { return reservations_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as RetriveResponse);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(RetriveResponse other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if(!reservations_.Equals(other.reservations_)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      hash ^= reservations_.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      reservations_.WriteTo(output, _repeated_reservations_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      reservations_.WriteTo(ref output, _repeated_reservations_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      size += reservations_.CalculateSize(_repeated_reservations_codec);
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(RetriveResponse other) {
      if (other == null) {
        return;
      }
      reservations_.Add(other.reservations_);
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            reservations_.AddEntriesFrom(input, _repeated_reservations_codec);
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            reservations_.AddEntriesFrom(ref input, _repeated_reservations_codec);
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code
