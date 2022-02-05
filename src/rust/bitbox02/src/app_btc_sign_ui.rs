// Copyright 2021 Shift Crypto AG
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

use alloc::boxed::Box;

use util::c_types::c_char;

pub struct Ui {
    pub verify_recipient: Box<dyn Fn(&str, &str) -> bool>,
    pub verify_total: Box<dyn Fn(&str, &str) -> bool>,
    pub confirm: Box<dyn Fn(&str, &str) -> bool>,
}
unsafe impl Sync for Ui {}

static mut UI: Option<Ui> = None;

/// This sets the callback functions in testing that will be used by btc_sign.c to perform blocking
/// UI operations.
pub fn mock(ui: Ui) {
    unsafe {
        UI = Some(ui);
    }
    unsafe extern "C" fn c_verify_recipient(
        recipient: *const c_char,
        amount: *const c_char,
    ) -> bool {
        let recipient = crate::util::str_from_null_terminated_ptr(recipient).unwrap();
        let amount = crate::util::str_from_null_terminated_ptr(amount).unwrap();
        (UI.as_ref().unwrap().verify_recipient)(recipient, amount)
    }
    unsafe extern "C" fn c_verify_total(total: *const c_char, fee: *const c_char) -> bool {
        let total = crate::util::str_from_null_terminated_ptr(total).unwrap();
        let fee = crate::util::str_from_null_terminated_ptr(fee).unwrap();
        (UI.as_ref().unwrap().verify_total)(total, fee)
    }
    unsafe extern "C" fn c_confirm(params: *const bitbox02_sys::confirm_params_t) -> bool {
        let title = crate::util::str_from_null_terminated_ptr((*params).title).unwrap();
        let body = crate::util::str_from_null_terminated_ptr((*params).body).unwrap();
        (UI.as_ref().unwrap().confirm)(title, body)
    }

    unsafe {
        bitbox02_sys::testing_app_btc_mock_ui(bitbox02_sys::app_btc_ui_t {
            verify_recipient: Some(c_verify_recipient),
            verify_total: Some(c_verify_total),
            confirm: Some(c_confirm),
        })
    }
}
