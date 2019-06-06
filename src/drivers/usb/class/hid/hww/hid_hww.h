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

#ifndef _HID_HWW_H_
#define _HID_HWW_H_

#include "hid.h"

/**
 * Sets the buffer address for the outgoing endpoint.
 * The length of the data to be written is defined in USB_HID_REPORT_OUT_SIZE.
 * @param[IN] size The size of the buffer.
 */
int32_t hid_hww_write(uint8_t *buf);

/**
 * Initializes a HWW HID interface.
 * @param[in] callback The callback that is called upon status update (enabling/disabling or the endpoints).
 */
int32_t hid_hww_init(void (*callback)(void));

/**
 * Deinitializes the HWW HID interface.
 */
int32_t hid_hww_deinit(void);

/**
 * Checks whether the HWW HID interface was enabled.
 */
bool hid_hww_is_enabled(void);

/**
 * Returns the version of the HWW interface.
 */
uint32_t hid_hww_get_version(void);

/**
 * Returns the endpoint for the given direction.
 * @param[in] dir The direction of the endpoint:
 *            dir == 1: outgoing (host -> BitBox)
 *            dir == 0: incoming (BitBox -> host)
 */
uint8_t hid_hww_get_ep(uint8_t dir);

/**
 * Registers a callback for a given transfer type.
 * @param[in] trans_type The transfer type for which the callback should be registered,
 *            which can be READ, WRITE or SET_REPORT.
 * @param[in] func The function that is registered as a callback.
 */
int32_t hid_hww_register_callback(enum hid_trans_type trans_type, FUNC_PTR func);

/**
 * Registers the HID HWW read and write callbacks and start listening for data.
 */
void hid_hww_setup(void);

#endif
