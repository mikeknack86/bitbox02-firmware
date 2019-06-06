// Copyright 2019 Shift Cryptosecurity AG
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "curve_p256.h"
#include "pukcc.h"

#define CURVE_TEST_MSG_LEN 4u
#define CURVE_TEST_MSG "abcd"

#if (CURVE_TEST_MSG_LEN > PUKCC_ECC_TEST_MSG_MAX_LEN)
#error "macro mismatch"
#endif

// clang-format off
__attribute__((aligned(4))) const PUKCC_CURVE_256_X curve_p256 = {
    // Elliptical curve equation:  x^3 = x^2 + a*x + b
    .a = {
        0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x01,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfc,
    },
    .b = {
        0x5a, 0xc6, 0x35, 0xd8, 0xaa, 0x3a, 0x93, 0xe7,
        0xb3, 0xeb, 0xbd, 0x55, 0x76, 0x98, 0x86, 0xbc,
        0x65, 0x1d, 0x06, 0xb0, 0xcc, 0x53, 0xb0, 0xf6,
        0x3b, 0xce, 0x3c, 0x3e, 0x27, 0xd2, 0x60, 0x4b,
    },
    .modulo_p = {
        0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x01,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
    },
    .base_x = {
        0x6b, 0x17, 0xd1, 0xf2, 0xe1, 0x2c, 0x42, 0x47,
        0xf8, 0xbc, 0xe6, 0xe5, 0x63, 0xa4, 0x40, 0xf2,
        0x77, 0x03, 0x7d, 0x81, 0x2d, 0xeb, 0x33, 0xa0,
        0xf4, 0xa1, 0x39, 0x45, 0xd8, 0x98, 0xc2, 0x96,
    },
    .base_y = {
        0x4f, 0xe3, 0x42, 0xe2, 0xfe, 0x1a, 0x7f, 0x9b,
        0x8e, 0xe7, 0xeb, 0x4a, 0x7c, 0x0f, 0x9e, 0x16,
        0x2b, 0xce, 0x33, 0x57, 0x6b, 0x31, 0x5e, 0xce,
        0xcb, 0xb6, 0x40, 0x68, 0x37, 0xbf, 0x51, 0xf5,
    },
    .order = {
        0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0xbc, 0xe6, 0xfa, 0xad, 0xa7, 0x17, 0x9e, 0x84,
        0xf3, 0xb9, 0xca, 0xc2, 0xfc, 0x63, 0x25, 0x51,
    },
    .one = {
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01,
    },
    .zero = {
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    },
    //
    // Unit test variables
    //
    .test_message_len = CURVE_TEST_MSG_LEN,
    .test_message = CURVE_TEST_MSG,
    // SHA256 of message
    .test_message_hash = {
        0x88, 0xd4, 0x26, 0x6f, 0xd4, 0xe6, 0x33, 0x8d,
        0x13, 0xb8, 0x45, 0xfc, 0xf2, 0x89, 0x57, 0x9d,
        0x20, 0x9c, 0x89, 0x78, 0x23, 0xb9, 0x21, 0x7d,
        0xa3, 0xe1, 0x61, 0x93, 0x6f, 0x03, 0x15, 0x89,
    },
    .test_private_key = {
        0x90, 0x43, 0xc2, 0xae, 0x42, 0x77, 0x13, 0xe8,
        0x68, 0xd9, 0x12, 0x86, 0x2c, 0x7b, 0xbf, 0x58,
        0x61, 0x15, 0x07, 0xf7, 0x30, 0xf0, 0x36, 0x0b,
        0x2d, 0x95, 0xc9, 0xc4, 0x2d, 0xa0, 0x03, 0x90,
    },
    .test_public_key = {
        0x23, 0x55, 0x1b, 0xc3, 0xdb, 0x0a, 0x24, 0x18,
        0xb0, 0x10, 0xf3, 0x13, 0x95, 0x9d, 0xab, 0x96,
        0xc0, 0xae, 0x9a, 0xa4, 0x3d, 0xc7, 0x42, 0xa9,
        0xb6, 0xc8, 0xd7, 0x73, 0xe0, 0x29, 0x94, 0x2a,
        0x2c, 0x71, 0x25, 0x46, 0x61, 0x55, 0x18, 0xf9,
        0x5b, 0x3c, 0xe1, 0xb1, 0xd1, 0x71, 0x62, 0x3f,
        0xe6, 0x89, 0x08, 0x4a, 0xce, 0x03, 0x28, 0x52,
        0xf2, 0xe1, 0x4e, 0xa5, 0xc4, 0x37, 0x84, 0xf5,
    },
    // Note: use deterministic K (RFC 6979) in production
    .test_k = {
        0xaa, 0x97, 0x78, 0xfc, 0xee, 0x7f, 0xdb, 0x15,
        0x8c, 0x1f, 0x3e, 0xda, 0xf6, 0x92, 0x49, 0xc7,
        0xb3, 0xce, 0x20, 0xa1, 0x1f, 0x46, 0x4c, 0xfe,
        0xdd, 0x9c, 0x91, 0x9a, 0x69, 0x9f, 0x23, 0xd1,
    },
    // Expected signature of message
    .test_signature = {
        // high-s
        0xb2, 0x98, 0x15, 0xfb, 0x68, 0x82, 0x4e, 0x8a,
        0x2f, 0xdf, 0x3c, 0x62, 0x3f, 0x1a, 0x23, 0x20,
        0x86, 0xcc, 0xe1, 0x64, 0xf0, 0x73, 0xcb, 0xc9,
        0xb9, 0x4e, 0x25, 0x5a, 0x1b, 0xf5, 0xfd, 0x6e,
        0xa7, 0x48, 0x3a, 0xeb, 0x51, 0x87, 0x8a, 0xf3,
        0x93, 0xb1, 0xe6, 0xf4, 0xa3, 0x74, 0x53, 0xa6,
        0xdb, 0x90, 0xa9, 0xcd, 0x1c, 0x7a, 0xdb, 0x46,
        0x3f, 0x5f, 0x68, 0x42, 0xec, 0xd8, 0x76, 0x32,
        /*// low-s (normalized)
        0xb2, 0x98, 0x15, 0xfb, 0x68, 0x82, 0x4e, 0x8a,
        0x2f, 0xdf, 0x3c, 0x62, 0x3f, 0x1a, 0x23, 0x20,
        0x86, 0xcc, 0xe1, 0x64, 0xf0, 0x73, 0xcb, 0xc9,
        0xb9, 0x4e, 0x25, 0x5a, 0x1b, 0xf5, 0xfd, 0x6e,
        0x58, 0xb7, 0xc5, 0x13, 0xae, 0x78, 0x75, 0x0d,
        0x6c, 0x4e, 0x19, 0x0b, 0x5c, 0x8b, 0xac, 0x58,
        0xe1, 0x56, 0x50, 0xe0, 0x8a, 0x9c, 0xc3, 0x3e,
        0xb4, 0x5a, 0x62, 0x80, 0x0f, 0x8a, 0xaf, 0x1f,
        */
    },
};
// clang-format on
