import 'package:json_annotation/json_annotation.dart';

part 'server_api.g.dart';

@JsonSerializable()
class ServerUser {
  final String uri;

  ServerUser(this.uri);

  factory ServerUser.fromJson(Map<String, dynamic> json) => _$ServerUserFromJson(json);
  Map<String, dynamic> toJson() => _$ServerUserToJson(this);
}

@JsonSerializable()
class ServerItem {
  final String title;
  final String content;

  const ServerItem(this.title, this.content);

  factory ServerItem.fromJson(Map<String, dynamic> json) => _$ServerItemFromJson(json);
  Map<String, dynamic> toJson() => _$ServerItemToJson(this);
}
