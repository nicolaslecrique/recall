import 'dart:io';

import 'package:http/http.dart' as http;
import 'package:recall_app/models/server_api.dart';

import '../app_config.dart';

class Server {
  static Future<ServerUser> getUser(String jwtToken) async {
    var result = await http.get(
      Uri.parse("${AppConfig.apiUrl}/user"),
      headers: {
        HttpHeaders.authorizationHeader: 'Bearer $jwtToken',
      },
    );

    return ServerUser("uri");
  }
}
