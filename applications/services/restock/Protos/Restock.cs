// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: restock.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Restock.Protos {

  /// <summary>Holder for reflection information generated from restock.proto</summary>
  public static partial class RestockReflection {

    #region Descriptor
    /// <summary>File descriptor for restock.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static RestockReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "Cg1yZXN0b2NrLnByb3RvEgdyZXN0b2NrGhtnb29nbGUvcHJvdG9idWYvZW1w",
            "dHkucHJvdG8itgEKDlJlc3RvY2tSZXF1ZXN0EhMKC3JlcXVlc3RUZXh0GAEg",
            "ASgJEjIKCGl0ZW1UeXBlGAIgASgOMiAucmVzdG9jay5SZXN0b2NrUmVxdWVz",
            "dC5JdGVtVHlwZRIZChFleGlzdGluZ0l0ZW1Db3VudBgDIAEoBRIPCgdzdG9y",
            "ZUlkGAQgASgFEg4KBml0ZW1JZBgFIAEoCSIfCghJdGVtVHlwZRIICgRCT09L",
            "EAASCQoFVklOWUwQATJQCgtSZXN0b2NrR3JwYxJBCg5SZXF1ZXN0UmVzdG9j",
            "axIXLnJlc3RvY2suUmVzdG9ja1JlcXVlc3QaFi5nb29nbGUucHJvdG9idWYu",
            "RW1wdHlCEaoCDlJlc3RvY2suUHJvdG9zYgZwcm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Google.Protobuf.WellKnownTypes.EmptyReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Restock.Protos.RestockRequest), global::Restock.Protos.RestockRequest.Parser, new[]{ "RequestText", "ItemType", "ExistingItemCount", "StoreId", "ItemId" }, null, new[]{ typeof(global::Restock.Protos.RestockRequest.Types.ItemType) }, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class RestockRequest : pb::IMessage<RestockRequest>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<RestockRequest> _parser = new pb::MessageParser<RestockRequest>(() => new RestockRequest());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<RestockRequest> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Restock.Protos.RestockReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public RestockRequest() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public RestockRequest(RestockRequest other) : this() {
      requestText_ = other.requestText_;
      itemType_ = other.itemType_;
      existingItemCount_ = other.existingItemCount_;
      storeId_ = other.storeId_;
      itemId_ = other.itemId_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public RestockRequest Clone() {
      return new RestockRequest(this);
    }

    /// <summary>Field number for the "requestText" field.</summary>
    public const int RequestTextFieldNumber = 1;
    private string requestText_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string RequestText {
      get { return requestText_; }
      set {
        requestText_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "itemType" field.</summary>
    public const int ItemTypeFieldNumber = 2;
    private global::Restock.Protos.RestockRequest.Types.ItemType itemType_ = global::Restock.Protos.RestockRequest.Types.ItemType.Book;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Restock.Protos.RestockRequest.Types.ItemType ItemType {
      get { return itemType_; }
      set {
        itemType_ = value;
      }
    }

    /// <summary>Field number for the "existingItemCount" field.</summary>
    public const int ExistingItemCountFieldNumber = 3;
    private int existingItemCount_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int ExistingItemCount {
      get { return existingItemCount_; }
      set {
        existingItemCount_ = value;
      }
    }

    /// <summary>Field number for the "storeId" field.</summary>
    public const int StoreIdFieldNumber = 4;
    private int storeId_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int StoreId {
      get { return storeId_; }
      set {
        storeId_ = value;
      }
    }

    /// <summary>Field number for the "itemId" field.</summary>
    public const int ItemIdFieldNumber = 5;
    private string itemId_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string ItemId {
      get { return itemId_; }
      set {
        itemId_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as RestockRequest);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(RestockRequest other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (RequestText != other.RequestText) return false;
      if (ItemType != other.ItemType) return false;
      if (ExistingItemCount != other.ExistingItemCount) return false;
      if (StoreId != other.StoreId) return false;
      if (ItemId != other.ItemId) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (RequestText.Length != 0) hash ^= RequestText.GetHashCode();
      if (ItemType != global::Restock.Protos.RestockRequest.Types.ItemType.Book) hash ^= ItemType.GetHashCode();
      if (ExistingItemCount != 0) hash ^= ExistingItemCount.GetHashCode();
      if (StoreId != 0) hash ^= StoreId.GetHashCode();
      if (ItemId.Length != 0) hash ^= ItemId.GetHashCode();
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
      if (RequestText.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(RequestText);
      }
      if (ItemType != global::Restock.Protos.RestockRequest.Types.ItemType.Book) {
        output.WriteRawTag(16);
        output.WriteEnum((int) ItemType);
      }
      if (ExistingItemCount != 0) {
        output.WriteRawTag(24);
        output.WriteInt32(ExistingItemCount);
      }
      if (StoreId != 0) {
        output.WriteRawTag(32);
        output.WriteInt32(StoreId);
      }
      if (ItemId.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(ItemId);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (RequestText.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(RequestText);
      }
      if (ItemType != global::Restock.Protos.RestockRequest.Types.ItemType.Book) {
        output.WriteRawTag(16);
        output.WriteEnum((int) ItemType);
      }
      if (ExistingItemCount != 0) {
        output.WriteRawTag(24);
        output.WriteInt32(ExistingItemCount);
      }
      if (StoreId != 0) {
        output.WriteRawTag(32);
        output.WriteInt32(StoreId);
      }
      if (ItemId.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(ItemId);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (RequestText.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(RequestText);
      }
      if (ItemType != global::Restock.Protos.RestockRequest.Types.ItemType.Book) {
        size += 1 + pb::CodedOutputStream.ComputeEnumSize((int) ItemType);
      }
      if (ExistingItemCount != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(ExistingItemCount);
      }
      if (StoreId != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(StoreId);
      }
      if (ItemId.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(ItemId);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(RestockRequest other) {
      if (other == null) {
        return;
      }
      if (other.RequestText.Length != 0) {
        RequestText = other.RequestText;
      }
      if (other.ItemType != global::Restock.Protos.RestockRequest.Types.ItemType.Book) {
        ItemType = other.ItemType;
      }
      if (other.ExistingItemCount != 0) {
        ExistingItemCount = other.ExistingItemCount;
      }
      if (other.StoreId != 0) {
        StoreId = other.StoreId;
      }
      if (other.ItemId.Length != 0) {
        ItemId = other.ItemId;
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
            RequestText = input.ReadString();
            break;
          }
          case 16: {
            ItemType = (global::Restock.Protos.RestockRequest.Types.ItemType) input.ReadEnum();
            break;
          }
          case 24: {
            ExistingItemCount = input.ReadInt32();
            break;
          }
          case 32: {
            StoreId = input.ReadInt32();
            break;
          }
          case 42: {
            ItemId = input.ReadString();
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
            RequestText = input.ReadString();
            break;
          }
          case 16: {
            ItemType = (global::Restock.Protos.RestockRequest.Types.ItemType) input.ReadEnum();
            break;
          }
          case 24: {
            ExistingItemCount = input.ReadInt32();
            break;
          }
          case 32: {
            StoreId = input.ReadInt32();
            break;
          }
          case 42: {
            ItemId = input.ReadString();
            break;
          }
        }
      }
    }
    #endif

    #region Nested types
    /// <summary>Container for nested types declared in the RestockRequest message type.</summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static partial class Types {
      public enum ItemType {
        [pbr::OriginalName("BOOK")] Book = 0,
        [pbr::OriginalName("VINYL")] Vinyl = 1,
      }

    }
    #endregion

  }

  #endregion

}

#endregion Designer generated code
