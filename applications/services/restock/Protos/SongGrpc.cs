// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: song.proto
// </auto-generated>
#pragma warning disable 0414, 1591
#region Designer generated code

using grpc = global::Grpc.Core;

namespace Metadata.Protos {
  /// <summary>
  ///Song servicer
  ///Only has CRUD methods, as it is only used for meta data
  /// </summary>
  public static partial class Song
  {
    static readonly string __ServiceName = "Song";

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static void __Helper_SerializeMessage(global::Google.Protobuf.IMessage message, grpc::SerializationContext context)
    {
      #if !GRPC_DISABLE_PROTOBUF_BUFFER_SERIALIZATION
      if (message is global::Google.Protobuf.IBufferMessage)
      {
        context.SetPayloadLength(message.CalculateSize());
        global::Google.Protobuf.MessageExtensions.WriteTo(message, context.GetBufferWriter());
        context.Complete();
        return;
      }
      #endif
      context.Complete(global::Google.Protobuf.MessageExtensions.ToByteArray(message));
    }

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static class __Helper_MessageCache<T>
    {
      public static readonly bool IsBufferMessage = global::System.Reflection.IntrospectionExtensions.GetTypeInfo(typeof(global::Google.Protobuf.IBufferMessage)).IsAssignableFrom(typeof(T));
    }

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static T __Helper_DeserializeMessage<T>(grpc::DeserializationContext context, global::Google.Protobuf.MessageParser<T> parser) where T : global::Google.Protobuf.IMessage<T>
    {
      #if !GRPC_DISABLE_PROTOBUF_BUFFER_SERIALIZATION
      if (__Helper_MessageCache<T>.IsBufferMessage)
      {
        return parser.ParseFrom(context.PayloadAsReadOnlySequence());
      }
      #endif
      return parser.ParseFrom(context.PayloadAsNewBuffer());
    }

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Metadata.Protos.CreateSongRequest> __Marshaller_CreateSongRequest = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Metadata.Protos.CreateSongRequest.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Metadata.Protos.CreateSongResponse> __Marshaller_CreateSongResponse = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Metadata.Protos.CreateSongResponse.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Metadata.Protos.GetSongByIdRequest> __Marshaller_GetSongByIdRequest = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Metadata.Protos.GetSongByIdRequest.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Metadata.Protos.GetSongByIdResponse> __Marshaller_GetSongByIdResponse = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Metadata.Protos.GetSongByIdResponse.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Metadata.Protos.UpdateSongRequest> __Marshaller_UpdateSongRequest = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Metadata.Protos.UpdateSongRequest.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Metadata.Protos.UpdateSongResponse> __Marshaller_UpdateSongResponse = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Metadata.Protos.UpdateSongResponse.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Metadata.Protos.DeleteSongByIdRequest> __Marshaller_DeleteSongByIdRequest = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Metadata.Protos.DeleteSongByIdRequest.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Metadata.Protos.DeleteSongByIdResponse> __Marshaller_DeleteSongByIdResponse = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Metadata.Protos.DeleteSongByIdResponse.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Metadata.Protos.GetAllSongsRequest> __Marshaller_GetAllSongsRequest = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Metadata.Protos.GetAllSongsRequest.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Metadata.Protos.GetAllSongsResponse> __Marshaller_GetAllSongsResponse = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Metadata.Protos.GetAllSongsResponse.Parser));

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Metadata.Protos.CreateSongRequest, global::Metadata.Protos.CreateSongResponse> __Method_createSong = new grpc::Method<global::Metadata.Protos.CreateSongRequest, global::Metadata.Protos.CreateSongResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "createSong",
        __Marshaller_CreateSongRequest,
        __Marshaller_CreateSongResponse);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Metadata.Protos.GetSongByIdRequest, global::Metadata.Protos.GetSongByIdResponse> __Method_getSongById = new grpc::Method<global::Metadata.Protos.GetSongByIdRequest, global::Metadata.Protos.GetSongByIdResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "getSongById",
        __Marshaller_GetSongByIdRequest,
        __Marshaller_GetSongByIdResponse);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Metadata.Protos.UpdateSongRequest, global::Metadata.Protos.UpdateSongResponse> __Method_updateSong = new grpc::Method<global::Metadata.Protos.UpdateSongRequest, global::Metadata.Protos.UpdateSongResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "updateSong",
        __Marshaller_UpdateSongRequest,
        __Marshaller_UpdateSongResponse);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Metadata.Protos.DeleteSongByIdRequest, global::Metadata.Protos.DeleteSongByIdResponse> __Method_deleteSongById = new grpc::Method<global::Metadata.Protos.DeleteSongByIdRequest, global::Metadata.Protos.DeleteSongByIdResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "deleteSongById",
        __Marshaller_DeleteSongByIdRequest,
        __Marshaller_DeleteSongByIdResponse);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Metadata.Protos.GetAllSongsRequest, global::Metadata.Protos.GetAllSongsResponse> __Method_getAllSongs = new grpc::Method<global::Metadata.Protos.GetAllSongsRequest, global::Metadata.Protos.GetAllSongsResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "getAllSongs",
        __Marshaller_GetAllSongsRequest,
        __Marshaller_GetAllSongsResponse);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::Metadata.Protos.SongReflection.Descriptor.Services[0]; }
    }

    /// <summary>Client for Song</summary>
    public partial class SongClient : grpc::ClientBase<SongClient>
    {
      /// <summary>Creates a new client for Song</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public SongClient(grpc::ChannelBase channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for Song that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public SongClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      protected SongClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      protected SongClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      /// <summary>
      ///CreateSong - Creates and persist new Song
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Metadata.Protos.CreateSongResponse createSong(global::Metadata.Protos.CreateSongRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return createSong(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      ///CreateSong - Creates and persist new Song
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Metadata.Protos.CreateSongResponse createSong(global::Metadata.Protos.CreateSongRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_createSong, null, options, request);
      }
      /// <summary>
      ///CreateSong - Creates and persist new Song
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Metadata.Protos.CreateSongResponse> createSongAsync(global::Metadata.Protos.CreateSongRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return createSongAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      ///CreateSong - Creates and persist new Song
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Metadata.Protos.CreateSongResponse> createSongAsync(global::Metadata.Protos.CreateSongRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_createSong, null, options, request);
      }
      /// <summary>
      ///GetSongById - Returns Song based on ID
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Metadata.Protos.GetSongByIdResponse getSongById(global::Metadata.Protos.GetSongByIdRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return getSongById(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      ///GetSongById - Returns Song based on ID
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Metadata.Protos.GetSongByIdResponse getSongById(global::Metadata.Protos.GetSongByIdRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_getSongById, null, options, request);
      }
      /// <summary>
      ///GetSongById - Returns Song based on ID
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Metadata.Protos.GetSongByIdResponse> getSongByIdAsync(global::Metadata.Protos.GetSongByIdRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return getSongByIdAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      ///GetSongById - Returns Song based on ID
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Metadata.Protos.GetSongByIdResponse> getSongByIdAsync(global::Metadata.Protos.GetSongByIdRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_getSongById, null, options, request);
      }
      /// <summary>
      ///UpdateSong - Updates info on existing Song
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Metadata.Protos.UpdateSongResponse updateSong(global::Metadata.Protos.UpdateSongRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return updateSong(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      ///UpdateSong - Updates info on existing Song
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Metadata.Protos.UpdateSongResponse updateSong(global::Metadata.Protos.UpdateSongRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_updateSong, null, options, request);
      }
      /// <summary>
      ///UpdateSong - Updates info on existing Song
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Metadata.Protos.UpdateSongResponse> updateSongAsync(global::Metadata.Protos.UpdateSongRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return updateSongAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      ///UpdateSong - Updates info on existing Song
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Metadata.Protos.UpdateSongResponse> updateSongAsync(global::Metadata.Protos.UpdateSongRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_updateSong, null, options, request);
      }
      /// <summary>
      ///DeleteSong - Deletes Song based on ID
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Metadata.Protos.DeleteSongByIdResponse deleteSongById(global::Metadata.Protos.DeleteSongByIdRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return deleteSongById(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      ///DeleteSong - Deletes Song based on ID
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Metadata.Protos.DeleteSongByIdResponse deleteSongById(global::Metadata.Protos.DeleteSongByIdRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_deleteSongById, null, options, request);
      }
      /// <summary>
      ///DeleteSong - Deletes Song based on ID
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Metadata.Protos.DeleteSongByIdResponse> deleteSongByIdAsync(global::Metadata.Protos.DeleteSongByIdRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return deleteSongByIdAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      ///DeleteSong - Deletes Song based on ID
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Metadata.Protos.DeleteSongByIdResponse> deleteSongByIdAsync(global::Metadata.Protos.DeleteSongByIdRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_deleteSongById, null, options, request);
      }
      /// <summary>
      ///GetAllSongs - Retrieves all songs from DB
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Metadata.Protos.GetAllSongsResponse getAllSongs(global::Metadata.Protos.GetAllSongsRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return getAllSongs(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      ///GetAllSongs - Retrieves all songs from DB
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Metadata.Protos.GetAllSongsResponse getAllSongs(global::Metadata.Protos.GetAllSongsRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_getAllSongs, null, options, request);
      }
      /// <summary>
      ///GetAllSongs - Retrieves all songs from DB
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Metadata.Protos.GetAllSongsResponse> getAllSongsAsync(global::Metadata.Protos.GetAllSongsRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return getAllSongsAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      ///GetAllSongs - Retrieves all songs from DB
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Metadata.Protos.GetAllSongsResponse> getAllSongsAsync(global::Metadata.Protos.GetAllSongsRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_getAllSongs, null, options, request);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      protected override SongClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new SongClient(configuration);
      }
    }

  }
}
#endregion
