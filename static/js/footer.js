document.addEventListener("DOMContentLoaded", function () {
  // 수신 이메일 설정
  const email = "haeengin@gmail.com";

  // 메일 제목 설정
  const subject = encodeURIComponent("HaeengIn의 웹 사이트 문의");

  // 현재 날짜 및 시간 설정 (KST)
  const now = new Date();
  const kstOffset = 9 * 60;
  const utc = now.getTime() + now.getTimezoneOffset() * 60000;
  const kstDate = new Date(utc + kstOffset * 60000);
  const today = kstDate.toISOString().split("T")[0];
  const currentTime = kstDate.toTimeString().split(" ")[0];

  // 메일이 생성된 링크 설정
  const fromUrl = window.location.href;

  // 유저 브라우저 정보 설정
  const userAgent = navigator.userAgent;
  const platform = navigator.platform;
  const screenSize = `${screen.width}x${screen.height}`;
  const viewportSize = `${window.innerWidth}x${window.innerHeight}`;
  const isMobile = /Android|iPhone|iPad|iPod/i.test(userAgent)
    ? "모바일"
    : "데스크탑";

  // 메일 본문 작성
  const body = encodeURIComponent(
    `문의 메일 생성 날짜: ${today} - ${currentTime} (KST)
문의 생성 링크: ${fromUrl}

[브라우저 정보]
접속 기기: ${isMobile}
OS/플랫폼: ${platform}
브라우저 UA: ${userAgent}
화면 해상도: ${screenSize}
뷰포트 크기: ${viewportSize}

내용: `,
  );

  // footer 설정
  const hr = document.createElement("hr");
  const footer = document.createElement("footer");
  const copyright = document.createElement("p");
  copyright.innerHTML = "Copyright 2026 &copy; HaeengIn. All Rights Reserved.";
  const report = document.createElement("a");
  report.classList.add("footer");
  report.href = `mailto:${email}?subject=${subject}&body=${body}`;
  report.target = "_blank";
  report.rel = "noopener noreferrer";
  report.textContent = "오류 신고";

  const contact = document.createElement("a");
  contact.classList.add("footer");
  contact.href = `mailto:${email}`;
  contact.target = "_blank";
  contact.rel = "noopener noreferrer";
  contact.textContent = "문의하기";
  footer.appendChild(hr);
  footer.appendChild(copyright);
  footer.appendChild(report);
  footer.appendChild(contact);
  document.body.appendChild(footer);
});
