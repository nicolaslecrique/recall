// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'server_api.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ServerUser _$ServerUserFromJson(Map<String, dynamic> json) => ServerUser(
      json['uri'] as String,
    );

Map<String, dynamic> _$ServerUserToJson(ServerUser instance) =>
    <String, dynamic>{
      'uri': instance.uri,
    };

ServerItem _$ServerItemFromJson(Map<String, dynamic> json) => ServerItem(
      json['title'] as String,
      json['content'] as String,
    );

Map<String, dynamic> _$ServerItemToJson(ServerItem instance) =>
    <String, dynamic>{
      'title': instance.title,
      'content': instance.content,
    };
